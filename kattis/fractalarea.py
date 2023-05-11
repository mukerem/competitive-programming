# https://open.kattis.com/problems/fractalarea
# Time: 2022-09-07 19:39:10
# title: Fractal Area
# language: Python 3


from math import pi
def a(r):
    return pi*r*r
for _ in range(int(input())):
    r, n = map(int, input().split())
    if n == 1:
        print(a(r))
    elif n == 2:
        print(a(r) + 4 * a(r/2))
    else:
        b = a(r) + 4 * a(r/2)
        r = r/4
        c = 12
        for i in range(n-2):
            d = a(r) * c
            r = r/2
            c = c*3
            b += d
        print(b)