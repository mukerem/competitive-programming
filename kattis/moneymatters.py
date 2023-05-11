# https://open.kattis.com/problems/moneymatters
# Time: 2022-09-10 16:29:07
# title: Money Matters
# language: Python 3


'''
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
q = []
c = 0
for i in range(1, n+1):
    b = a[:i]
    b = sum(b) /100
    c += b/i
    if b == 0:
        q.append(0)
    else:
        q.append(pow(b, b/i) * c)
print(sum(q)/n/c)
'''
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
s = [i for i in range(n)]
def root(x):
    while s[x]!= x:
        x = s[x]
    return x
    
for i in range(m):
    u, v = map(int, input().split())
    x = root(u)
    y = root(v)
    s[x] = y

d = {}
f = 1
for idx, i in enumerate(s):
    x = root(idx)
    #print(x)
    if x in d:
        d[x].append(idx)
    else:
        d[x] = [idx]

for i in d:
    k = d[i]
    t = 0
    for j in k:
        t += a[j]
    if t != 0:
        print('IMPOSSIBLE')
        break
else:
    print('POSSIBLE')
