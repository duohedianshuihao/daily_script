from models import QuestionDAO


def get_answer(question_str, answer_l):
    answer_dao = QuestionDAO.get_correct_answer(question_str)
    if answer_dao is not None:
        return answer_dao.answer

    question_dao = QuestionDAO.get_question(question_str)
    if not question_dao:
        QuestionDAO.create_question(question_str, answer_l)
        question_dao = QuestionDAO.get_question(question_str)

    answer_str = _get_random_answer(question_dao)
    return answer_str


def _get_random_answer(question_dao):
    for dao in question_dao:
        if dao.correct == 0:
            continue
        return dao.answer


def mark_answer(question_str, answer_str, res):
    dao = QuestionDAO.get_question_answer(question_str, answer_str)
    if dao is None:
        raise Exception
    dao.mark_answer(res)
