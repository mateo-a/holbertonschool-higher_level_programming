#!/usr/bin/python3
"""

Function that returns a list of lists of integers representing
the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """Returns a list of lists of integers for the Pascal’s triangle
    Args:
        n (int): number
    """
    if n <= 0:
        return []
    triangle = []
    for row in range(1, n + 1):
        temp = []
        for i in range(row):
            if i == 0 or i == row - 1:
                temp.append(1)
            else:
                temp.append(triangle[row - 2][i] + triangle[row - 2][i - 1])
        triangle.append(temp)
    return(triangle)
