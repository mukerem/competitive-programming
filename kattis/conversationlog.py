# https://open.kattis.com/problems/conversationlog
# Time: 2022-09-18 21:16:30
# title: Conversation Log
# language: Python 3


a = {}
c = []
for i in range(int(input())):
    x = input().split()
    y = x[0]
    x = x[1:]
    if y in a:
        a[y].extend(x)
    else:
        a[y] = x
    c.extend(x)
c = list(set(c))
d = []
m = len(a)
for i in c:
    q = 0
    for j in a:
        if not i in a[j]:
            break
        q += a[j].count(i)
    else:
        d.append((-q, i))
if d:
    d.sort()
    for i, v  in d:
        print(v)
else:
    print('ALL CLEAR')