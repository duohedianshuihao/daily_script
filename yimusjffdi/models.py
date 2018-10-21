from peewee import MySQLDatabase, Model, IntegerField, CharField, BooleanField
from config import DBConfig


mysql_db = MySQLDatabase(DBConfig.DATABASE,
                         user=DBConfig.USER,
                         password=DBConfig.PASSWORD,
                         host=DBConfig.HOST,
                         port=DBConfig.PORT)


class QuestionDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'question'

    id = IntegerField(5)
    question = CharField(200)
    answer = CharField(200)
    correct = BooleanField(default=None)

    @classmethod
    def get_question(cls, question_str):
        return list(cls.select().where(cls.question == question_str).execute())

    @classmethod
    def get_correct_answer(cls, question_str):
        return cls.get_or_none(cls.question == question_str, cls.correct == 1)

    @classmethod
    def get_question_answer(cls, question_str, answer_str):
        return cls.get_or_none(cls.question == question_str, cls.answer == answer_str)

    @classmethod
    def create_question(cls, question_str, answer_l):
        for _answer in answer_l:
            cls.create(question=question_str, answer=_answer)
        return

    def mark_answer(self, res):
        self.update(correct=res)
