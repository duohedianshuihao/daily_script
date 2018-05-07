# coding: utf-8

import random
import string
import getopt
import sys


def get_random_string(length=15):
    print ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(int(length)))


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'l:')
    except getopt.GetoptError:
        sys.stdout.write("NOTE: ignoring args rather than -l, using default length 15\n")
        get_random_string()
    else:
        opts_d = {t[0]: t[1] for t in opts}
        get_random_string(opts_d.get('-l', 15))
