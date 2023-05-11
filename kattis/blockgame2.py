# https://open.kattis.com/contests/dp2yve
# Time: 2022-09-15 18:37:50
# title: EtCPC2022 - Practice - 7 / Block Game
# language: Python 3


a,b = map(int, input().split())
if a<b:a,b=b,a
if a%b == 0:
    print('win')
elif a > 2*b:
    print('win')
else:
    c = 0
    while a<2*b:
        a,b = b, a-b
        c += 1
    if c%2 == 0:
        print('win')
    else:
        print('lose')
    