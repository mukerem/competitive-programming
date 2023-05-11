# https://open.kattis.com/problems/tourdefrance
# Time: 2022-09-09 19:27:19
# title: Tour de France
# language: Python 3


while 1:
    x = input()
    if x == '0':
        break
    f, r = map(int, x.split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for v in a:
        d = []
        for u in b:
            c.append(u/v)
        
    #c = list(set(c))
    c.sort()
    m = 0
    for i in range(len(c)-1):
        q = c[i+1]/c[i]
        m = max(m, q)
    print("%.2f" % m)
    