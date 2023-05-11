# https://open.kattis.com/problems/runningsteps
# Time: 2022-10-08 13:04:18
# title: Running Steps
# language: Python 3


from math import factorial
for _ in range(int(input())):
    kk, s = map(int, input().split())
    x = s//2
    y = 0
    ans = 0
    while x >= y:
        if x%2 == 0:
            k = x//2
            u = y//2
            #print(k, u)
            v = factorial(k+u)//factorial(k)//factorial(u)
            ans += v*v
        x -= 1
        y += 2
    print(kk, ans)
