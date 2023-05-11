# https://open.kattis.com/problems/woodcutting
# Time: 2022-09-09 19:47:16
# title: Wood Cutting
# language: Python 3


for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x = list(map(int, input().split()))
        y = sum(x[1:])
        a.append(y)
    a.sort()
    t = 0
    s = 0
    for i in a:
        t += i
        s += t
    print(s / n)
