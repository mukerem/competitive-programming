# https://open.kattis.com/problems/sretan
# Time: 2022-09-09 20:24:53
# title: Sretan
# language: Python 3


n = int(input())
a = []
t = 2
s = 2
k = 1
while s < n:
    t *= 2
    s += t
    k += 1
x = s-n
x = bin(x)[2:]
x = '0'*(k-len(x)) + x
y = x.replace('0', '7').replace('1', '4')
print(y)
