# coding: utf-8

from requests_html import HTMLSession

PAGE = input("enter page address here: ")
TYPE = input("file type: ")


def get_link():
    session = HTMLSession()
    r = session.get(PAGE)
    for link in r.html.absolute_links:
        if link.split(".")[-1] == TYPE:
            print(link)


if __name__ == '__main__':
    get_link()
