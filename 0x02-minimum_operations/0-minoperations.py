#!/usr/bin/python3

"""
    Method that determines the number of minimum operations given n characters
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly n H characters in a file.

    Args:
        n (int): Number of characters to be displayed.

    Returns:
        int: Number of minimum operations.
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
