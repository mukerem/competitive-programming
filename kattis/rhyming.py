# https://open.kattis.com/contests/nms22o
# Time: 2022-09-04 16:26:41
# title: EtCPC2022 - Practice - 2 / Rhyming Slang
# language: Python 3


c = input().lower()
n = int(input())

b = []
for _ in range(n):
    s = input().lower().split()
    b.append(s)

n = int(input())
for _ in range(n):
    s = input().lower()
    
    for i in b:
        x = False
        y = False
        for j in i:
            if j == c[-len(j):]:
                x = True
            if j == s[-len(j):]:
                y = True
        if x and y:
           print('YES')
           break
    else:
        print('NO')
