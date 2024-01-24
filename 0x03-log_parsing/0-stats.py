#!/usr/bin/python3

""" A script that reads stdin line by line and computes metrics """

import sys


def printStatus(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for x in sorted(dic.keys()):
        if dic[x] != 0:
            print("{}: {:d}".format(x, dic[x]))


# sourcery skip: use-contextlib-suppress
statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

idx = 0
size = 0

try:
    for line in sys.stdin:
        if idx != 0 and idx % 10 == 0:
            printStatus(statusCodes, size)

        stlist = line.split()
        idx += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in statusCodes:
                statusCodes[stlist[-2]] += 1
        except Exception:
            pass
    printStatus(statusCodes, size)


except KeyboardInterrupt:
    printStatus(statusCodes, size)
    raise
