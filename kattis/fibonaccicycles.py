# https://open.kattis.com/problems/fibonaccicycles
# Time: 2022-09-18 14:55:39
# title: Fibonacci Cycles
# language: Python 3


for _ in range(int(input())):
    k = int(input())
    b = {}
    x = 1
    y = 1
    i = 2
    while 1:
        z = (x+y)%k
        if z in b:
            print(b[z])
            break
        b[z] = i
        i += 1
        x = y
        y = z