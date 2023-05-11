# https://open.kattis.com/problems/lamps
# Time: 2022-09-07 20:05:03
# title: Lamps
# language: Python 3


x, p = map(int, input().split())

from math import ceil
def fun(h):
    k1 = 60*h*p / 100000 + 5 * ceil(h/1000)
    k2 = 11*h*p/ 100000 + 60* ceil(h/8000)
    return k1,k2
    
h = 1
while True:
    a, b = fun(h)
    if a >= b:
        print(int(ceil(h/x)))
        break
    h += 1
        