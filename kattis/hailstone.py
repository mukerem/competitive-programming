# https://open.kattis.com/contests/ao8dza
# Time: 2020-12-17 20:25:27
# title: Day10Night / Watch Out For Those Hailstones!
# language: Python 3


n = int(input())
s = n
while n != 1:
    if n% 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    s += n

print(s)
