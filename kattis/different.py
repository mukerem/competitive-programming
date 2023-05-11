# https://open.kattis.com/problems/different
# Time: 2022-09-16 16:08:50
# title: A Different Problem
# language: Python 3


while 1:
    try:
        a,b = map(int, input().split())
        print(abs(a-b))
    except:
        break