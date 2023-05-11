# https://open.kattis.com/contests/nms22o
# Time: 2022-09-04 11:30:01
# title: EtCPC2022 - Practice - 2 / Playfair Cipher
# language: Python 3


a = input()
b = input()
a = a.replace(' ', '').upper()
b = b.replace(' ', '').upper()
c = [['' for i in range(5)] for j in range(5)]
d = [chr(i+65) for i in range(26)]
d.remove('Q')
x = 0
y = 0

for i in a+''.join(d):
    if not i in d:
        continue
    c[x][y] = i
    y += 1
    if y == 5:
        x += 1
        y = 0
    d.remove(i)
m = {}
for i in range(5):
    for j in range(5):
        m[c[i][j]] = (i,j)
s = ''
i = 0
while i < len(b):
    u = b[i]
    if i+1 == len(b):
        v = 'X'
    else:
        v = b[i+1]
    if u == v:
        v = 'X'
        i += 1
    else:
        i += 2
    
    r1,c1 = m[u]
    r2,c2 = m[v]
    if r1 == r2:
        s += c[r1][(c1+1)%5]
        s += c[r2][(c2+1)%5]
    elif c1 == c2:
        s += c[(r1+1)%5][c1]
        s += c[(r2+1)%5][c2]
    else:
        s += c[r1][c2]
        s += c[r2][c1]
print(s)
