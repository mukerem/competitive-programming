# https://open.kattis.com/contests/r72fms
# Time: 2021-09-20 18:42:02
# title: CPD Day 6 / Riječi
# language: Python 3


n = int(input())
a = [0, 1]
for i in range(n-1):
      a.append(a[-1] + a[-2])
print(a[-2], a[-1])
