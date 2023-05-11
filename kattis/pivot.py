# https://open.kattis.com/problems/pivot
# Time: 2022-09-26 21:23:41
# title: Pivot
# language: Python 3


n = int(input())
a = list(map(int, input().split()))
b = a[:]
b.sort()
q = {}
for i, v in enumerate(b):
    q[v] = i
c = 0
m = -1000000000000
for i in range(n):
    h = a[i]
    p = q[h]
    if p == i and h > m:
        c += 1
    m = max(m, h)
print(c)
    
    