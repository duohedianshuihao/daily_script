# coding: utf-8

import requests_html as request
import simplejson as json
# from multiprocessing import Pool

COMPANY = input("the company you want: ")


def get_target_problems(session, url, page, result):
    curr_url = url + "page={}".format(page)
    resp = session.get(curr_url)
    problems = json.loads(resp.content)["problems"]
    for problem in problems:
        if problem.get("company_tags"):
            if COMPANY in problem["company_tags"]:
                result.append((problem["id"], problem["title"]))


def get_pages(session, url):
    resp = session.get(url)
    return json.loads(resp.content)["maximum_page"]


def main():
    session = request.HTMLSession()
    url = "https://www.lintcode.com/api/problems/?"
    pages = get_pages(session, url)
    result = []
    for page in range(1, pages + 1):
        get_target_problems(session, url, page, result)
    result.sort(key=lambda problem: problem[0])
    for line in result:
        print(line)
    print(len(result))


if __name__ == '__main__':
    main()
