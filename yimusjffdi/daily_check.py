import requests
from fake_useragent import FakeUserAgent

QUESTION_URL = "https://www.1point3acres.com/bbs/plugin.php?id=ahome_dayquestion:pop&infloat=yes&handlekey=pop&inajax=1&ajaxtarget=fwin_content_pop"
ANSWER_URL = "https://www.1point3acres.com/bbs/plugin.php?id=ahome_dayquestion:index"

CHECKIN_URL = "https://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&74889ea9&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign"
SUBMIT_URL = "https://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1"


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
        cookie_str = fd.readlines()[0]

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


# def make_answer():


def send_request(headers, cookies):
    session = requests.Session()
    resp = session.get(url=CHECKIN_URL, headers=headers, cookies=cookies)
    print(resp.status_code)
    print(resp.content.decode(encoding="gbk"))


def checkin_request(headers, cookies, data):
    session = requests.Session()
    resp = session.post(url=SUBMIT_URL, headers=headers, cookies=cookies, data=data)
    print(resp.status_code)
    print(resp.content.decode(encoding="gbk"))


def main():
    headers = make_header()
    cookies = make_cookies()
    data = make_data()
    # send_request(headers, cookies)
    checkin_request(headers, cookies, data)


if __name__ == '__main__':
    main()
