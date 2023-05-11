# https://open.kattis.com/contests/uybefk
# Time: 2019-11-27 10:12:25
# title: CPC Wednesday #10 / Some Sum
# language: Python 2


n = input()
if n%2 == 1:
    print 'Either'
else:
    n /= 2
    if n%2 == 0:
        print 'Even'
    else:
        print 'Odd'
