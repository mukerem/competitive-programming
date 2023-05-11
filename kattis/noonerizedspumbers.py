# https://open.kattis.com/problems/noonerizedspumbers
# Time: 2022-09-08 23:08:10
# title: Noonerized Spumbers
# language: Python 3


d = input()
a,c = d.split(' = ')
if '*' in a:
    o = '*'     
    a,b = a.split(' * ')
else:
    o = '+'
    a,b = a.split(' + ')
def evaluation():
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            x = b[:j] + a[i:]
            y = a[:i] + b[j:]
            z = c
            if eval(x+o+y) == int(z):
                print(x,o,y,'=',z)
                return
    for i in range(1, len(c)):
        for j in range(1, len(b)):
            z = b[:j] + c[i:]
            y = c[:i] + b[j:]
            x = a
            if eval(x+o+y) == int(z):
                print(x,o,y,'=',z)
                return
    for i in range(1, len(a)):
        for j in range(1, len(c)):
            x = c[:j] + a[i:]
            z = a[:i] + c[j:]
            y = b
            if eval(x+o+y) == int(z):
                print(x,o,y,'=',z)
                return
evaluation()
