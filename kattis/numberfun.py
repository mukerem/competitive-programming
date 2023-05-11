# https://open.kattis.com/contests/bgyhnz
# Time: 2019-11-27 17:03:25
# title: CSC Weekly Challenge 5 / Number Fun
# language: Python 2


n = input()
for i in range(n):
    a,b,c = [int(k) for k in raw_input().split()]
    if a+b == c:
        print 'Possible'
    elif a*b == c:
        print 'Possible'
    elif abs(a-b) == c:
        print 'Possible'
    elif a == b* c:
        print 'Possible'
    elif b == a * c:
        print 'Possible'
    else:
        print 'Impossible'
