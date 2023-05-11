# https://open.kattis.com/contests/r72fms
# Time: 2021-09-20 18:21:26
# title: CPD Day 6 / 3D Printed Statues
# language: Python 3


n = int(input())
from math import log, ceil
a = int(ceil(log(n) / log(2)))
print(a+1)
