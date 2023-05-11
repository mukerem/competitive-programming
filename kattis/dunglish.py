# https://open.kattis.com/problems/dunglish
# Time: 2022-09-09 10:07:41
# title: Dunglish
# language: Python 3


n = int(input())
a = input().split()
b = {}
u = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
    u[i] = 0 
m = int(input())
c = []
trans = {}
cor = 'correct'
v = {}
for i in range(m):
    x,y,z = input().split()
    trans[x] = y
    c.append(x)
    if z == 'incorrect':
        cor = 'incorrect'
    else:
        if x in u:
            u[x] += 1
        
    if x in v:
        v[x] += 1
    else:
        v[x] = 1

ans1 = 1
ans2 = 1
for i in u:
    if i in b:
        ans1 *= u[i] ** b[i]
for i in v:
    if i in b:
        ans2 *= (v[i]) ** b[i]
ans2 -= ans1

if ans1 == 1 and ans2 == 0:
    for i in a:
        print(trans[i], end=' ')
    print()
    print('correct')
elif ans1 == 0 and ans2 == 1:
    for i in a:
        print(trans[i], end=' ')
    print()
    print('incorrect')
else:
    print(ans1, 'correct')
    print(ans2, 'incorrect')