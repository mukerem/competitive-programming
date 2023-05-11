# https://open.kattis.com/problems/memorymatch
# Time: 2022-09-06 10:10:26
# title: Memory Match
# language: Python 3


n = int(input())
k = int(input())
a = {}
b = 0
c = []
for i in range(k):
    x,y,u,v = input().split()
    x = int(x)
    y = int(y)
    if u == v:
        b += 2
        if u in a:
            a.pop(u)
        continue
    if u in a:
        a[u].add(x)
    else:
        a[u] = {x}
    
    if v in a:
        a[v].add(y)
    else:
        a[v] = {y}

d = 0
r = 0
for i in a:
    if len(a[i]) == 2:
        d += 1
        b += 2
    else:
        r += 1
z = n - b - r
if z == r:
    d += z
if r == 0 and z == 2:
    d += 1
print(d)
