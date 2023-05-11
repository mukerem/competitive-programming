# https://open.kattis.com/problems/ornaments
# Time: 2022-09-03 08:36:14
# title: Ornaments
# language: Python 3


from math import pi, sqrt, atan2
while 1:
    r,h,s = map(int, input().split())
    if r+h+s==0:
        break
    y = r*r / h
    if r < y:
        x = 0
    else:
        x = sqrt(r*r - y*y)
    t = atan2(y, x)
    alp = pi + 2 * t
    per = r * alp
    b = 2 * sqrt(x*x + (y-h) ** 2)
    l = b + per
    l += l * s / 100
    print('%.2f' % l)
