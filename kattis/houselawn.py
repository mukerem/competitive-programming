# https://open.kattis.com/problems/houselawn
# Time: 2022-09-08 19:59:04
# title: House Lawn
# language: Python 3


l, m = map(int, input().split())
a = []
from math import ceil
def price(n,p,c,t,r, idx):
    for T in range(1,20000):
        time = T * 10080
        x = time//(r+t)
        z = time % (r+t)
        z = min(z, t)
        h = x * c * t + z*c
        if h < T*l:
            return
    a.append((p, idx,n))
    
for i in range(m):
    n,p,c,t,r = input().split(',')
    p = int(p)
    c = int(c)
    t = int(t)
    r = int(r)
    price(n,p,c,t,r,i)

a.sort()
if a:
    m = a[0][0]
    for i,j,k in a:
        if i == m:
            print(k)
        
else:
    print('no such mower')
