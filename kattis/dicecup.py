# https://open.kattis.com/problems/dicecup
# Time: 2019-09-25 12:13:14
# title: Dice Cup
# language: Python 2


a,b = [int(i) for i in raw_input().split()]
for i in range(min(a,b) + 1, max(a,b) + 2):
    print i
