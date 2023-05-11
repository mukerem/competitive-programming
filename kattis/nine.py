# https://open.kattis.com/problems/nine
# Time: 2019-11-17 14:53:12
# title: I Hate The Number Nine
# language: Python 2


m = 1000000007
for i in range(input()):
    x = input()
    z = pow(9, x-1, m)
    print(z * 8)%m
