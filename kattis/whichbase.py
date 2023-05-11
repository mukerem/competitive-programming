# https://open.kattis.com/problems/whichbase
# Time: 2022-09-08 22:36:26
# title: Which Base is it Anyway?
# language: Python 3


for _ in range(int(input())):
    k, n = map(int, input().split())
    n = str(n)
    print(k, end= ' ')
    if '8' in n or '9' in n:
        print(0, end=' ')
    else:
        print(int(n, 8), end = ' ')
    print(n, int(n, 16))
