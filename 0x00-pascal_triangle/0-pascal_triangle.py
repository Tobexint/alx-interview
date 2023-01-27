#!/usr/bin/python3
""" Pascal's triangle
"""


def pascal_triangle(n):
    """returns a list of lists representing Pascal's triangle"""
    lst = []
    if (n <= 0):
        return lst
    lst.append([1])
    for i in range(n -1):
        lst.append([1] + [lst[i][j] + lst[i][j + 1]
                    for j in range(len(lst[i]) - 1)] + [1])
    return lst
