# https://open.kattis.com/problems/oddities
# Time: 2019-08-19 18:27:09
# title: Oddities
# language: Python 2


n = input()
for i in range(n):
    a = input()
    if a%2:
        print a, 'is odd'
    else:
        print a, 'is even'
