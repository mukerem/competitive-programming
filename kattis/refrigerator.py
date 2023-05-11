# https://open.kattis.com/problems/refrigerator
# Time: 2022-09-21 16:47:29
# title: Refrigerator Transport
# language: Python 3


pa, ka, pb, kb, n = map(int, input().split())

def cost(x, y):
    a = (x + ka-1) // ka
    b = (y + kb-1) // kb
    p = pa * a + pb * b
    return p,a,b
a = []
for i in range(n+1):
    p = cost(i, n-i)
    a.append(p)
x = min(a)
print(x[1],x[2], x[0])