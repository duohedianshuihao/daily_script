# coding: utf-8

"""
logging to the router at home to get device name at home right now, based on requests Python 2.7.14
"""

import requests
import time
import os

URL = os.environ.get('HOME_LOGIN_URL', None)
USER = os.environ.get('HOME_USER', None)
PASSWORD = os.environ.get('HOME_PASSWORD', None)
USER_LIST_URL = os.environ.get('HOME_USER_LIST_URL', None)


class CouldNotGetEnviron(Exception):
    pass


class TimedOut(Exception):
    pass


def main():
    if not all([URL, USER, PASSWORD, USER_LIST_URL]):
        raise CouldNotGetEnviron
    s = requests.Session()
    data = {
        'user': USER,
        'pws': PASSWORD
    }
    try:
        r = s.post(URL, data=data)
    except requests.exceptions.ConnectionError:
        raise TimedOut
    if r.status_code != 200:
        return
    params = {'_': int(time.time() * 1000)}
    users = s.get(USER_LIST_URL, params=params)
    for user in eval(users.content):
        hostName = user.get('hostName', None).lower()
        if not hostName or hostName == 'unknown':
            continue
        print hostName


if __name__ == '__main__':
    main()
