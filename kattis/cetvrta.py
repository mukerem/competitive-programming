# https://open.kattis.com/problems/cetvrta
# Time: 2019-08-19 22:52:59
# title: Cetvrta
# language: Python 2


a = []
b = []
for i in range(3):
    x , y =[int(k) for k in raw_input().split()]
    if x in a:
        a.remove(x)
    else:
        a.append(x)
    if y in b:
        b.remove(y)
    else:
        b.append(y)
print a[0],b[0]
