#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row.

    Args:
    n (int): Number of rows in Pascal's triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # Define a row and fill first and last indices with 1
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1

        for j in range(1, i):
            if 0 < j < len(row):
                x = pascal_triangle[i - 1][j]
                y = pascal_triangle[i - 1][j - 1]
                row[j] = x + y

        pascal_triangle[i] = row

    return pascal_triangle
