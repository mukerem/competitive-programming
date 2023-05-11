# https://open.kattis.com/problems/chess
# Time: 2022-09-18 22:09:08
# title: Chess
# language: Python 3


for i in range(int(input())):
    a,b,c,d = input().split()
    a = ord(a) - 64
    c = ord(c) - 64
    b = int(b)
    d = int(d)
    e = abs(a-c) + abs(b-d)
    if e % 2 == 1:
        print('Impossible')
        continue
    if a == c and b == d:
        print(0, chr(a+64), b)
    elif a+b == c+d or a-b == c-d:
        print(1,  chr(a+64), b,  chr(c+64), d)
    else:
        # u, v
        # a+b = u+v and u-v = c-d
        # 2u = a+b+c-d
        # u = (a+b+c-d)/2
        # v = a+b-u
        u = (a+b+c-d)
        if u%2 == 0:
            u = u // 2
            v = a+b-u
            if 1<= u<= 8 and 1<= v<= 8:
                print(2,  chr(a+64), b,  chr(u+64), v, chr(c+64), d)
                continue
        # a-b = u-v and u+v = c+d
        # 2u = a+c+d-b
        # u = (a-b+c+d)/2
        # v = a+b-u
        u = (a-b+c+d)
        u = u // 2
        v = c+d-u
        print(2,  chr(a+64), b,  chr(u+64), v, chr(c+64), d)
                