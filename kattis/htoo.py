# https://open.kattis.com/problems/htoo
# Time: 2022-09-06 22:05:13
# title: H to O
# language: Python 3


a, b = input().split()
b = int(b)
c = {}
e = []
idx = 0
for i in a:
    if i.isalpha():
        e.append(idx)
    idx += 1
e.append(len(a))
for i in range(len(e)-1):
    u = e[i]+1
    v = e[i+1]
    if u == v:
        q = 1
    else:
        q = int(a[u:v])
    r = a[e[i]]
    if r in c:
        c[r] += b*q
    else:
        c[r] = b*q

a = input()
    
d = {}
e = []
idx = 0
for i in a:
    if i.isalpha():
        e.append(idx)
    idx += 1
e.append(len(a))
for i in range(len(e)-1):
    u = e[i]+1
    v = e[i+1]
    if u == v:
        q = 1
    else:
        q = int(a[u:v])
    r = a[e[i]]
    if r in d:
        d[r] += q
    else:
        d[r] = q

m = 10000000000
for i in d:
    u = d[i]
    if i in c:
        v = c[i]
    else:
        print(0)
        break
    m = min(m, v // u)
else:
    print(m)
