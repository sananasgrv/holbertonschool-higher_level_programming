#!/usr/bin/python3
"""Doc"""


def pascal_triangle(n):
    """Doc"""

    l = []
    if n <= 0:
        return l
    l = [1]
    for i in range(1, n):
        l.append(l[i] + l[i-1])
        if i == n-1:
            l.append(1)

    return l
