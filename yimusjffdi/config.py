import os


class DBConfig(object):
    """
    parameters for database connection
    """
    DATABASE = os.getenv("_DATABASE")
    USER = os.getenv("_USER")
    PASSWORD = os.getenv("_PASSWORD")
    HOST = os.getenv("_HOST")
    PORT = int(os.getenv("_PORT"))


class URLConfig(object):
    """
    all the url info for daily checkin and answering question
    """
    QUESTION_URL = "https://www.1point3acres.com/bbs/plugin.php?id=ahome_dayquestion:pop&infloat=yes&handlekey=pop&inajax=1&ajaxtarget=fwin_content_pop"
    ANSWER_URL = "https://www.1point3acres.com/bbs/plugin.php?id=ahome_dayquestion:pop"

    CHECKIN_URL = "https://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&74889ea9&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign"
    SUBMIT_URL = "https://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1"


WRONG = "抱歉，回答错误！扣除1大米"
