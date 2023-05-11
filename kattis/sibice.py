# https://open.kattis.com/problems/sibice
# Time: 2019-08-19 18:00:33
# title: Sibice
# language: Python 2


n,w,h = [int(i) for i in raw_input().split()]
from math import sqrt
r = sqrt(w*w + h*h)
for i in range(n):
    x = input()
    if x<= r:
        print 'DA'
    else:
        print 'NE'
