# https://open.kattis.com/problems/zipline
# Time: 2022-09-09 21:54:49
# title: Zipline
# language: Python 3


from math import sqrt
def fun(w,g,h,r,k):
    T = k* sqrt((w-k)**2 + h**2) - (w-k)*sqrt(k**2 + g**2)
    return T
        
    
for _ in range(int(input())):
    w,g,h,r = map(int, input().split())
    minn = (w*w + abs(g-h) ** 2) ** 0.5
    g -= r
    h -= r
    left = 0
    right = w
    while right - left > 1e-6:
        k = (left+right)/2
        d = fun(w,g,h,r,k)
        if d < 0:
            left = k
        else:
            right = k
    k = (left+right)/2
    maxx = sqrt(k**2 + g**2) + sqrt((w-k) ** 2 + h ** 2)
    print(minn, maxx)
