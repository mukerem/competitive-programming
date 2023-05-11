# https://open.kattis.com/problems/pot
# Time: 2019-08-19 18:20:01
# title: Pot
# language: Python 2


n = input()
sum = 0.0
from math import pow
for  i in range(n):
    a = raw_input()
    sum += pow(int(a[:-1]), int(a[-1]))
print int(sum)
