# https://open.kattis.com/problems/anthonyanddiablo
# Time: 2019-11-08 15:07:59
# title: Anthony and Diablo
# language: Python 2


from math import pi

a , p = [float(i) for i in raw_input().split()]
if a <= p*p/(4*pi):
    print 'Diablo is happy!'
else:
    print 'Need more materials!'
