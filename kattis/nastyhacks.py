# https://open.kattis.com/problems/nastyhacks
# Time: 2019-08-19 18:31:48
# title: Nasty Hacks
# language: Python 2


n = input()
for i in range(n):
    a,b,c = [int(j) for  j in raw_input().split()]
    if a + c == b:
        print 'does not matter'
    elif a+c<b:
        print 'advertise'
    else:
        print 'do not advertise'
