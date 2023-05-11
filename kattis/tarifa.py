# https://open.kattis.com/problems/tarifa
# Time: 2019-08-19 17:37:07
# title: Tarifa
# language: Python 2


x = input()
sum = 0;
n = input()
for i in range(n):
    b = input()
    sum += b
a = x * (n+1) - sum
#print sum
if a>0:
    print a
else:
    print 0
