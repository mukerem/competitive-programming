# https://open.kattis.com/problems/svada
# Time: 2022-09-04 15:07:54
# title: Svada
# language: Python 3


t = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))
m = int(input())
b = []
for i in range(m):
    b.append(tuple(map(int, input().split())))

from math import ceil
def fun(k):
    d = 0
    for x, y in a:
        z = k - x
        if z >= 0:
            d += z // y + 1
    
    e = 0
    for x, y in b:
        z = t - k - x
        if z >= 0:
            e += z // y + 1
    #print(k,d,e)
    if d <= e:
        return 1
    return -1

l = 0
r = t
u = 0
while l < r-1:
    m = (l+r)//2
    f = fun(m)
    #print(r,l,m,f)
    if f == -1:
        r = m
    else:
        l = m
else:
    for i in range(l, r+1):
        if fun(i) == 1:
            print(i)
            break
