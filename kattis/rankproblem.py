# https://open.kattis.com/problems/rankproblem
# Time: 2022-09-06 19:48:43
# title: A Rank Problem
# language: Python 3


n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
for i in range(m):
    x, y = input().split()
    x = int(x[1:])
    y = int(y[1:])
    u = a.index(x)
    v = a.index(y)
    if u > v:
        a.pop(v)
        a.insert(u, y)
for i in a:
        print(f'T{i}', end= ' ')
        
        