# https://open.kattis.com/problems/ljutnja
# Time: 2022-09-21 10:12:21
# title: Ljutnja
# language: Python 3


m, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
'''
c = a[:]
b = sum(a)
b -= m
x = b // n
y = b % n
for i in range(n):
    c[i] = x
for i in range(n-y, n):
    c[i] += 1
q = 0
d = 0
for i in range(n):
    q = m // n
    if a[i] > q:
        d = a[i]-q
        a[i] = q
        m -= d
    else:
        n -= 1
while m:
    
for i in a:
    z += i*i
print(z)
'''
a.reverse()
b = [0]
q = 0
for i in range(1, n):
    x = a[i-1] - a[i]
    if i*x <= m:
        b.append(x)
        m -= i*x
    else:
        q = i
        break
else:
    b.append(0)
    q = n
s = sum(b)
for i in range(q):
    
    s -= b[i]
    a[i] -= s

x = m // q
for i in range(q):
    a[i] -= x
for i in range(m%q):
    a[i] -= 1
z = 0
for i in a:
    z += i*i
print(z)
