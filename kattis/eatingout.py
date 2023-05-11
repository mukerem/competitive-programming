# https://open.kattis.com/problems/eatingout
# Time: 2022-09-05 21:00:10
# title: Eating Out
# language: Python 3


m,a,b,c = map(int, input().split())
if a+b+c > 2*m:
    print('impossible')
else:
    print('possible')