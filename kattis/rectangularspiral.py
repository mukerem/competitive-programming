# https://open.kattis.com/problems/rectangularspiral
# Time: 2022-09-02 16:19:11
# title: Growing Rectangular Spiral
# language: Python 3


for i in range(int(input())):
    k,x,y = map(int, input().split())
    if x == y:
        print(f'{k} NO PATH')
    elif x < y:
        print(f'{k} 2 {x} {y}')
    elif y < 4:
        print(f'{k} NO PATH')
    else:
        a = 4
        b = x + 2
        c = y + 2
        if c <= b:
            d = b + 1 - c
            c = b + 1
            a = a + d
        print(f'{k} 6 1 2 3 {a} {b} {c}')
