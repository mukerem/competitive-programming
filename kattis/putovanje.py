# https://open.kattis.com/problems/putovanje
# Time: 2022-09-20 15:22:05
# title: Putovanje
# language: Python 3


n, w = map(int, input().split())
a = list(map(int, input().split()))
c = 0
i = 0
m = 0
j = 0
for i in range(n):
    c = 0
    q = 0
    for j in range(i, n):
        if c + a[j] <= w:
            c += a[j]
            q += 1
    m = max(m, q)
print(m)