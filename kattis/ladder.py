# https://open.kattis.com/problems/ladder
# Time: 2019-08-19 19:30:18
# title: Ladder
# language: Python 2


from math import sin, pi, ceil
a,b = [int(i) for  i in raw_input().split()]
c = a/sin(b * pi/180.0)
print int(ceil(c))
