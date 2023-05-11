# https://open.kattis.com/problems/secretsanta
# Time: 2022-10-08 14:09:28
# title: Secret Santa
# language: Python 3


from math import factorial
n = int(input())
if n>15:
    print('0.6321205588285577')
    exit()
x = 1
y = 0
for i in range(1, n+1):
    x *= i
    y = y * i + (-1) ** (i+1)
print(y/x)
