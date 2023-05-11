# https://open.kattis.com/problems/parket
# Time: 2022-09-05 21:19:08
# title: Parket
# language: Python 3


r, bb = map(int, input().split())

# x row and y col of b
# L and W
# b = x*y
# r = 2x + 2y + 4
# x = r/2 - y - 2
# b = ry/2 - y^2 - 2y
# y**2 + (2-r/2)y +b=0
#l = x+2
#w = y+2
from math import sqrt
a = 1
b = 2 - r // 2
c = bb
x = (-b + sqrt(b*b - 4*a*c)) // 2
x = int(x)
y = bb // x
print(max(x, y) +2, min(x, y)+2)