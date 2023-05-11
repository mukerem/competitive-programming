# https://open.kattis.com/problems/zamka
# Time: 2019-08-18 20:03:34
# title: Zamka
# language: Python 2


l = input()
d = input()
x = input()
for i in range(l, d+1):
    a = [int (k) for k in str(i)]
    if sum(a) == x:
        print i
        break
    
for i in range(d, l-1, -1):
    a = [int (k) for k in str(i)]
    if sum(a) == x:
        print i
        break
