# https://open.kattis.com/problems/imperfectgps
# Time: 2022-09-13 09:18:17
# title: Imperfect GPS
# language: Python 3


n, t = map(int, input().split())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))
b = []
for i in range(n-1):
    x = a[i][-1]
    y = a[i+1][-1]
    d = y-x
    if x%t == 0:
        b.append(a[i])
    if y%t == 0:
        b.append(a[i+1])
    if x//t != y//t:
        z = (x//t+1)*t
        x1 = a[i][0]
        x2 = a[i+1][0]
        y1 = a[i][1]
        y2 = a[i+1][1]
        u = (x2-x1)/d
        v = (y2-y1)/d
        # y-y1 = m(x-x1)
        while z < y:
            x3 = x1 + u*(z-x)
            y3 = y1 + v*(z-x)
            b.append((x3, y3, z))
            z += t
x = a[-1]
if x[-1]%t != 0:
    b.append(x)
    
b = sorted(b, key=lambda x: x[-1])
x = 0
for i in range(len(a)-1):
    x1 = a[i][0]
    x2 = a[i+1][0]
    y1 = a[i][1]
    y2 = a[i+1][1]
    d = (x2-x1)**2 + (y2-y1)**2
    d = d ** 0.5
    x += d
    
y = 0
for i in range(len(b)-1):
    x1 = b[i][0]
    x2 = b[i+1][0]
    y1 = b[i][1]
    y2 = b[i+1][1]
    d = (x2-x1)**2 + (y2-y1)**2
    d = d ** 0.5
    y += d
    
z = x-y
print(z*100/x)
    

            
