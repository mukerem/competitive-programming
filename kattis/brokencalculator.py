# https://open.kattis.com/problems/brokencalculator
# Time: 2022-09-07 19:16:06
# title: Broken Calculator
# language: Python 3


n = 1
for _ in range(int(input())):
    x, y, z = input().split()
    x = int(x)
    z = int(z)
    if y == '+':
        n = (x+z) - n
    elif y == '-':
        n = n * (x-z)
    elif y == '*':
        n = (x*z)**2
    else:
        if x%2:
            n = (x+1)//2
        else:
            n = x // 2
    print(n)