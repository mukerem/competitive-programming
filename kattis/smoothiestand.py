# https://open.kattis.com/problems/smoothiestand
# Time: 2022-10-07 23:07:12
# title: Smoothie Stand
# language: Python 3


k, r = map(int, input().split())
m = 0
b = list(map(int, input().split()))
for i in range(r):
    x = list(map(int, input().split()))
    p = x[-1]
    x = x[:-1]
    c = []
    for idx, j in enumerate(x):
        if j:
            c.append(b[idx]//j)
    if c:
        m = max(m, p*min(c))
print(m)