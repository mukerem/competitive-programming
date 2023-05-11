# https://open.kattis.com/problems/diagonalcut
# Time: 2022-09-09 21:23:20
# title: Diagonal Cut
# language: Python 3


from math import gcd
a,b = map(int, input().split())
k = gcd(a, b)
x = a // k
y = b // k
if x%2 == 0 or y%2 == 0:
    print(0)
else:
    print(k)