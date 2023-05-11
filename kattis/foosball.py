# https://open.kattis.com/problems/foosball
# Time: 2022-09-08 09:30:35
# title: Foosball Dynasty
# language: Python 3


n = int(input())
a = input().split()
x = input()
p = 4
w = (a[0], a[2])
b = (a[1], a[3])
pw = 0
pb = 0
dy = []
ob = b
ow = w
for i in x:
    if i == 'W':
        if(pb > 0):dy.append((pb, -p, ob))
        pb = 0
        pw += 1
        loser = b[1]
        b = (a[p], b[0])
        w = (w[1], w[0])
        ob = b[::-1]
    else:
        if(pw > 0):dy.append((pw, -p, ow))
        pw = 0
        loser = w[1]
        w = (a[p], w[0])
        b = (b[1], b[0])
        pb += 1
        ow = w[::-1]
    p += 1
    a.append(loser)
if(pb > 0):dy.append((pb, -p, ob))
if(pw > 0):dy.append((pw, -p, ow))
dy.sort(reverse=True)
m = dy[0][0]
for i,j,k in dy:
    if i == m:
        print(*k)
    
