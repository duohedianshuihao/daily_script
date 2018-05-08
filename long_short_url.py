# coding: utf-8
"""
just a base62 convert method, Python 2.7.14
"""

import string

CHAR_D = {i: item for i, item in enumerate(string.ascii_letters + string.digits)}


def convert(number):
    if not isinstance(number, int):
        return
    base62_n = []
    while number > 0:
        number, reminder = divmod(number, 62)
        base62_n.append(reminder)
    print base62_n[::-1]
    s = ''.join(map(lambda x: CHAR_D[x], base62_n[::-1]))
    print s


if __name__ == '__main__':
    # 发号策略，对来的号码进行62进制编码，转换成短址
    convert(1234)
