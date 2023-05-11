# https://open.kattis.com/problems/lindenmayorsystem
# Time: 2022-09-03 21:30:49
# title: Linden Mayor System
# language: Python 3


n, m = map(int, input().split())
b = {}
for i in range(n):
    x,y = input().replace(' ', '').split('->')
    b[x] =  y
s = input()
for i in range(m):
    f = ''
    for k in s:
        if k in b:
            f += b[k]
        else:
            f += k
    s = f
print(s)
