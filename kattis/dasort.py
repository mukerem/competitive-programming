# https://open.kattis.com/problems/dasort
# Time: 2022-09-18 13:44:58
# title: DA-Sort
# language: Python 3


for _ in range(int(input())):
    a = []
    k, n = map(int, input().split())
    for i in range((n+9)//10):
        a.extend(list(map(int, input().split())))
    b = []
    for i,v in enumerate(a):
        b.append((v, i))
    b.sort()
    m = -1
    t = n
    q = -1
    for v, i in b:
        if i > m:
            m = i
            t -= 1
        else:
            q = v
            break
    if q != -1:
        for i,v in enumerate(a):
            if q == v and i > m:
                t -= 1
    print(k, t)