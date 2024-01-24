#!/usr/bin/python3

""" A script that reads stdin line by line and computes metrics """

import sys


def _printstat(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for x in sorted(dic.keys()):
        if dic[x] != 0:
            print("{}: {:d}".format(x, dic[i]))


# sourcery skip: use-contextlib-suppress
statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

cnt = 0
size = 0

try:
    for line in sys.stdin:
        if cnt != 0 and cnt % 10 == 0:
            _printstat(statusCodes, size)

        stlist = line.split()
        cnt += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in statusCodes:
                statusCodes[stlist[-2]] += 1
        except Exception:
            pass
    _printstat(statusCodes, size)


except KeyboardInterrupt:
    _printstat(statusCodes, size)
    raise
