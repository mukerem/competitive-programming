# https://open.kattis.com/problems/forestforthetrees
# Time: 2022-09-08 20:52:20
# title: Forest for the Trees
# language: Python 3


from math import gcd,ceil, floor
xb, yb = map(int, input().split())
x1,y1,x2,y2 = map(int, input().split())
k = gcd(xb, yb)
x = xb // k
y = yb // k

# kx1 = int(ceil(x1/x))
# kx2 = int(floor(x2/x))
kx1 = (x1+x-1) // x
kx2 = x2 // x


# ky1 = int(ceil(y1/y))
# ky2 = int(floor(y2/y))
ky1 = (y1+y-1) // y
ky2 = y2 // y


ka = min(kx2+1, ky2+1)
kb = min(kx1-1, ky1-1)
if k == 1:
    print('Yes')
elif x < x1 or y < y1:
    print('No')
    print(x, y)
elif (kb>0):
    print('No')
    print(x, y)
elif ka < k:
    print('No')
    print(ka*x, ka*y)
else:
    print('Yes')
