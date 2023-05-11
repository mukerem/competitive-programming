# https://open.kattis.com/problems/quadrant
# Time: 2019-08-18 19:55:42
# title: Quadrant Selection
# language: Python 2


x = input()
y = input()
if (x>0):
    if y>0:print 1
    else:print 4
else:
    if y>0:print 2
    else:print 3
