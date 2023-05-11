# https://open.kattis.com/problems/odds
# Time: 2022-08-30 12:21:09
# title: Odds of Mia
# language: Python 3


def mia(a,b,c,d):
    a,b = min(a,b), max(a,b)
    c,d = min(c,d), max(c,d)
    if a == c and b == d:
        return 0
    if c == 1 and d == 2:
        return 0
    if a == 1  and b == 2:
        return 1
    if a == b:
        if c == d:
            return a > c
        else:
            return 1
    if c == d:
        return 0
    return b*10+a > d*10+c

x = lambda a:  [1,2,3,4,5,6] if a == '*' else [int(a)]
while 1:
    f= input()
    if f == '0 0 0 0':
        break
    a,b,c,d = f.split()
    a = x(a)
    b = x(b)
    c = x(c)
    d = x(d)
    cou = 0
    tot = len(a) * len(b) * len(c) * len(d)
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    #print(i,j,k,l,mia(i,j,k,l))
                    cou += mia(i,j,k,l)
    if cou == 0 :
        print(0)
    elif cou == tot:
        print(1)
    else:
        from math import gcd
        g = gcd(cou, tot)
        cou = cou // g
        tot = tot // g
        print(f'{cou}/{tot}')
        
