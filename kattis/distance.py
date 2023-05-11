# https://open.kattis.com/problems/distance
# Time: 2022-09-26 21:51:25
# title: Distance
# language: Python 3


x = []
y = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
def distance(x):
    x.sort()
    a = []
    t = 0
    for i in x:
        t += i
        a.append(t)
    s = 0
    for i, r in enumerate(x):
        if i == 0:
            v = t-r
            d = v - r * (n-1)
        elif i == n-1:
            u = t - r
            d = r * (n-1) - u
        else:
            u = a[i-1]
            v = t - a[i]
            d = r*i - u + v - (r*(n-i-1))
        s += d
    return s
ans = distance(x) + distance(y)
print(ans//2)