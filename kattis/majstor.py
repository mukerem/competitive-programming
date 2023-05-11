# https://open.kattis.com/problems/majstor
# Time: 2022-09-03 21:01:02
# title: Majstor
# language: Python 3


n = int(input())
a = input()
m = int(input())
b = []
def score(x, y):
    z = 0
    for i,j in zip(x, y):
        if i == j:
            z+= 1
        elif i=='S' and j == 'P' or i == 'P' and j == 'R' or i == 'R' and j == 'S':
            z+=2
    return z
    
c = 0
for i in range(m):
    d = input()
    b.append(d)
    c += score(a, d)
e = 0
for i in range(len(a)):
    z = []
    for j in range(m):
        z.append(b[j][i])
    e += max(score(m*'S', z), score(m*'P', z), score(m*'R', z))
print(c)
print(e)
    
