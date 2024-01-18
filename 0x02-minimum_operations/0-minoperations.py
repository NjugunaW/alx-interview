#!/usr/bin/python3

"""
 This module calculates the fewest number of operations needed
"""


def minOperations(n):
    """
    This function calculates the lowest number of operations
    needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed

    Args:
        n:

    Returns:  number of min operations

    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if remainder % now == 0:
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
