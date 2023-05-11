# https://open.kattis.com/problems/arraysmoothening
# Time: 2022-09-18 14:46:48
# title: Array Smoothening
# language: Python 3



n, k = map(int, input().split())
a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
s = []
for i in b:
    s.append(b[i])
s.sort(reverse=True)
l = 0
r = max(s)
def count(m):
    d = 0
    for i in s:
        if i<=m:
            break
        d += (i-m)
    return d
while l<r:
    m = (l+r) // 2
    d = count(m)
    if d == k:
        r = m
        break
    if d>k:
        l = m+1
    else:
        r = m
print(r)