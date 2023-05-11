# https://open.kattis.com/problems/blackfriday
# Time: 2020-11-26 15:53:29
# title: Black Friday
# language: Python 2


n = input()
x = [int(i) for i in raw_input().split()]
y = []
for i in range(6, 0, -1):
    y.append((i, x.count(i)))
a = False

for i, j in y:
    if(j == 1):
        index =  i
        a = True
        break
if not a:
    print 'none'
else:
    print x.index(index) + 1
