import requests
from fake_useragent import FakeUserAgent
from bs4 import BeautifulSoup as Soup

from config import URLConfig, RIGHT
from utils import get_answer, mark_answer


def make_header():
    ua = FakeUserAgent()
    headers = {
        "User-Agent": ua.chrome,
        "Referer": "https: // www.1point3acres.com/bbs/",
        "Host": "www.1point3acres.com",
    }
    return headers


def make_cookies():
    with open("cookies.txt", "r+") as fd:
        cookie_str = fd.read()

    cookies = {}
    for item in cookie_str.split(";"):
        item = item.strip().split("=")
        cookies[item[0]] = item[1]
    return cookies


def make_data():
    data = {
        "formhash": "74889ea9",
        "qdxq": "kx",
        "qdmode": "2",
        "todaysay": "",
        "fastreply": "0"
    }
    return data


def get_question_detail(content):
    with open("temp.txt", "r+") as fd:
        content = fd.read()
    soup = Soup(content, "html.parser")

    question_str = soup.find('font').text.strip()

    answer_d = {}
    for item in soup.find_all("div", {"class": "qs_option"}):
        answer_d[item.text.strip()] = item.input["value"]
    return question_str, answer_d


def get_question(headers, cookies):
    session = requests.Session()
    resp = session.get(url=URLConfig.QUESTION_URL, headers=headers, cookies=cookies)

    if resp.status_code != 200:
        raise Exception
    return get_question_detail(resp.content.decode(encoding="gbk"))


def post_answer(headers, cookies):
    question_str, answer_d = get_question(headers, cookies)

    answer_str = get_answer(question_str, answer_d.keys())

    session = requests.Session()
    data = {
        "answer": answer_d[answer_str]
    }
    resp = session.post(url=URLConfig.ANSWER_URL, headers=headers, cookies=cookies, data=data)
    print(resp.content.decode(encoding="gbk"))

    soup = Soup(resp.content, "html.parser")
    res = True if soup.res.text == RIGHT else 0
    mark_answer(question_str, answer_str, res)


def post_checkin_request(headers, cookies, data):
    session = requests.Session()
    resp = session.post(url=URLConfig.SUBMIT_URL, headers=headers, cookies=cookies, data=data)
    print(resp.status_code)
    print(resp.content.decode(encoding="gbk"))


def main():
    headers = make_header()
    cookies = make_cookies()
    data = make_data()

    post_checkin_request(headers, cookies, data)
    post_answer(headers, cookies)


if __name__ == '__main__':
    main()
