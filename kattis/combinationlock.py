# https://open.kattis.com/problems/combinationlock
# Time: 2022-09-09 21:00:38
# title: Combination Lock
# language: Python 3


while 1:
    a,b,c,d = map(int, input().split())
    if a+b+c+d == 0:
        break
    x = 0
    x += 80
    if b<=a:
        x += (a-b)
    else:
        x += (40+a-b)
    
    x += 40

    if b<=c:
        x += (c-b)
    else:
        x += (40+c-b)
    
    if d<=c:
        x += (c-d)
    else:
        x += (40+c-d)
    print(x*9)
