#!/usr/bin/python3
"""Doc"""


def pascal_triangle(n):
    """Doc"""



    def summing(a,b,l: list ):
        l.append(a+b)
    prew = []
    now = []
    if n == 1:
        l = []
        return l
    for i in range(n):
        now.append(1)
        for j in range(i):
                summing(prew[j-1], prew[j], now)
        now.append(1)
        print(now)
        prew = now.copy()
        now = []