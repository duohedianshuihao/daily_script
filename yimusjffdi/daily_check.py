import requests
from fake_useragent import FakeUserAgent
from bs4 import BeautifulSoup as Soup

from config import URLConfig, WRONG
from utils import get_answer, mark_answer


def make_headers():
    ua = FakeUserAgent()
    headers = {
        "User-Agent": ua.chrome,
        "Referer": "https://www.1point3acres.com/bbs/",
        "Host": "www.1point3acres.com",
    }
    return headers


def make_cookies():
    # file_path = "change to cookies path"
    # file_name = "cookies.txt"
    with open("cookies.txt", "r+") as fd:
        cookie_str = fd.read()

    cookies = {}
    for item in cookie_str.split(";"):
        item = item.strip().split("=")
        cookies[item[0]] = item[1]
    return cookies


def get_question(headers, cookies):
    session = requests.Session()
    resp = session.get(url=URLConfig.QUESTION_URL, headers=headers, cookies=cookies)

    if resp.status_code != 200:
        raise Exception
    content = "".join(resp.text.split("\n")[2:-1])
    soup = Soup(content, "html.parser")

    question_str = soup.find('font').text.strip()

    answer_d = {}
    for item in soup.find_all("div", {"class": "qs_option"}):
        answer_d[item.text.strip()] = item.input["value"]
    return question_str, answer_d


def post_answer(headers, cookies):
    question_str, answer_d = get_question(headers, cookies)

    answer_str = get_answer(question_str, answer_d.keys())

    session = requests.Session()
    data = {
        "formhash": "74889ea9",
        "answer": answer_d[answer_str],
        "submit": "true"
    }
    resp = session.post(url=URLConfig.ANSWER_URL, headers=headers, cookies=cookies, data=data)

    soup = Soup(resp.text, "html.parser")
    res = soup.find("div", {"id": "messagetext"}).p.text
    print(res)
    correct = False if res == WRONG else True
    mark_answer(question_str, answer_str, correct)


def post_checkin_request(headers, cookies):
    session = requests.Session()
    data = {
        "formhash": "74889ea9",
        "qdxq": "kx",
        "qdmode": "2",
        "todaysay": "",
        "fastreply": "0"
    }
    resp = session.post(url=URLConfig.SUBMIT_URL, headers=headers, cookies=cookies, data=data)
    print(resp.status_code)
    print(resp.text)


def main():
    headers = make_headers()
    cookies = make_cookies()

    post_checkin_request(headers, cookies)
    post_answer(headers, cookies)


if __name__ == '__main__':
    main()
