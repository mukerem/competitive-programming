# https://open.kattis.com/problems/stirlingsapproximation
# Time: 2022-09-07 21:58:58
# title: Stirling's Approximation
# language: Python 3


from math import factorial, pi, sqrt, e, log
a = []
b = {}
while 1:
    n = int(input())
    if n == 0:
        break
    a.append(n)
    b[n] = 1
m = max(a)
f = 0
for i in range(1, m+1):
    f += log(i)
    if i in b:
        b[i] = f

for n in a:
    x = b[n] + n - n*log(n) - log(sqrt(2*pi*n))
    x = pow(e, x)
    print(x)
