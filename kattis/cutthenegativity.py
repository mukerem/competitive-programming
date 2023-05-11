# https://open.kattis.com/problems/cutthenegativity
# Time: 2023-03-05 12:05:07
# title: Cut the Negativity
# language: Python 3


n = int(input())
c=[]
for i in range(n):
    b = list(map(int, input().split()))
    c.append(b)
x = []
for i in range(n):
    for j in range(n):
        if c[i][j] != -1:
            x.append((i + 1, j + 1, c[i][j]))
print(len(x))
for i in x:
    print(*i)