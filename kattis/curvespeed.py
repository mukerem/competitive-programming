# https://open.kattis.com/problems/curvespeed
# Time: 2022-09-07 19:42:07
# title: Curve Speed
# language: Python 3


while 1:
    try:
        r,s = input().split()
        r = int(r)
        s = float(s)
        v = r * (s+0.16)/0.067
        v = v ** 0.5
        print(int(round(v)))
    except:
        break