# https://open.kattis.com/contests/kqzyje
# Time: 2019-11-28 13:31:46
# title: ASTU CPD CONTEST #2 / Missing Numbers
# language: Python 2


n = input()
i = 1
ok = True
for k in range(n):
    x = input()
    if x == i:
        i += 1
        continue
    for j in range(i, x):
        print j,
        ok = False
    i = x + 1
if ok:
    print 'good job'