# https://open.kattis.com/problems/slatkisi
# Time: 2019-11-28 08:58:14
# title: Slatkisi
# language: Python 2


n, k = [int(i) for i in raw_input().split()]
x = float(n) / (10 ** k)
y = round(x)
y *= (10**k)
y = int(y)
print y
