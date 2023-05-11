# https://open.kattis.com/problems/bootstrappingnumber
# Time: 2022-09-07 19:08:28
# title: Bootstrapping Number
# language: Python 3


a = 1
b = 10
n = int(input())
while abs(b-a) > 1e-6:
    c = (a+b)/2
    d = pow(c, c)
    if n < d:
        b = c
    else:
        a = c
print(a)
