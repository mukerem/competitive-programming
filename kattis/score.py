# https://open.kattis.com/contests/nms22o
# Time: 2022-09-04 11:03:05
# title: EtCPC2022 - Practice - 2 / Score!
# language: Python 3


a = 0
h = 0
c = []
for i in range(int(input())):
    x,y,z = input().split()
    y = int(y)
    u,v = map(int, z.split(':'))
    c.append((x,y,60*u+v))
x = 0
y = 0
z = 0
for i,j,k in c:
    if h>a:
        x += (k-z)
    elif h<a:
        y += (k-z)
    if i == 'H':
        h += j
    else:
        a += j
    z = k
if h>a:
    x += (32*60-z)
elif h<a:
    y += (32*60-z)
print(['A', 'H'][a<h], end=' ')
print(f'{x//60}:%s' % str(x%60).zfill(2), end=' ')
print(f'{y//60}:%s' % str(y%60).zfill(2))
