# https://open.kattis.com/problems/janitortroubles
# Time: 2019-10-02 19:55:52
# title: Janitor Troubles
# language: Python 2


from math import sqrt
a,b,c,d = [int(i) for i in raw_input().split()]
s = (a+b+c+d) / 2.0
area = sqrt((s - a) * (s-b) * (s - c) * (s-d))
print area
