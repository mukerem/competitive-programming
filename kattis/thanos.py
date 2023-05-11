# https://open.kattis.com/problems/thanos
# Time: 2019-11-16 22:28:57
# title: Thanos
# language: Python 2


for _ in range(input()):
    p,r,f = [int(i) for i in raw_input().split()]
    c = 0
    while f>=p:
        p = p*r
        c += 1
    print c