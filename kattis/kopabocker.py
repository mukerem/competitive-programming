# https://open.kattis.com/problems/kopabocker
# Time: 2022-09-05 23:50:06
# title: Buying Books
# language: Python 3


from itertools import combinations
n, m = map(int, input().split())
a = [i for i in range(m)]
b = []
for i in range(m):
    x, y = map(int, input().split())
    c = []
    for j in range(x):
        c.append(list(map(int, input().split())))
    b.append((y, c))
    
def cal(r):
    ans = 0
    q = [[] for i in range(n)]
    for v, i in r:
        ans += v
        for j, h in i:
            q[j-1].append(h)
    for i in q:
        if i == []:
            return -1
        ans += min(i)
    return ans
    
z = []
for i in range(1,m +1):
    z.extend(list(combinations(b, i)))
best = 1000000000000000000
for i in z:
    d = cal(i)
    if d != -1:
        best = min(best, d)
print(best)
