# https://open.kattis.com/contests/neeziy
# Time: 2019-11-26 17:35:13
# title: ASTU OS ICPC 1 / Yin and Yang Stones
# language: Python 3


x = input()
if x.count('W') == x.count('B'):
    print(1)
else:
    print(0)