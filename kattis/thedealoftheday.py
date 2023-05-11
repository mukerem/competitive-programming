# https://open.kattis.com/contests/uybefk
# Time: 2019-11-27 13:39:23
# title: CPC Wednesday #10 / The Deal of the Day
# language: Python 2


import itertools
a = [int(i) for i in raw_input().split()]
k = input()
x = list(itertools.combinations(a,k))
ans = 0
for i in x:
    y = 1
    for j in i:
        y *= j
    ans += y
print ans
