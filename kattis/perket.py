# https://open.kattis.com/problems/perket
# Time: 2022-09-03 20:49:44
# title: Perket
# language: Python 3


def sour(a):
    x = 1
    y = 0
    for i,j in a:
        x *= i
        y += j
    return abs(x-y)
from itertools import combinations
a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
x = []
for i in range(1, n+1):
    x.extend(list(combinations(a, i)))
b = 100000000000
for i in x:
    b = min(b, sour(i))
print(b)
