# https://open.kattis.com/problems/reducedidnumbers
# Time: 2022-09-09 22:11:57
# title: Reduced ID Numbers
# language: Python 3


g = int(input())
a = []
for i in range(g):
    a.append(int(input()))
for m in range(g, 1000000):
    b = {}
    for i in a:
        r = i%m 
        if r in b:
            break
        b[r] = True
    else:
        print(m)
        break