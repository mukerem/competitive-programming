# https://open.kattis.com/contests/neeziy
# Time: 2019-11-26 17:41:06
# title: ASTU OS ICPC 1 / Akcija
# language: Python 2


n = input()
x = []
for i in range(n):
    
    x.append(input())
x.sort(reverse = True)
ans = 0
for i in range(2, n, 3):
    ans += x[i]
print sum(x) - ans
