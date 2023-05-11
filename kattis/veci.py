# https://open.kattis.com/contests/seshqv
# Time: 2020-11-26 15:02:58
# title: ASTU-Tournament(2/5) / Veci
# language: Python 2


from itertools import permutations  
  
  
n = input()
x = list(str(n))
perm = permutations(x)
minn = 10000000
case = False
for i in list(perm):  
    num = int(''.join(i))
    if n < num:
        case = True
        if num < minn:
            minn = num
if case:
    print minn
else:
    print 0
