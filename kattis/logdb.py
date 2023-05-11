# https://open.kattis.com/contests/dp2yve
# Time: 2022-09-15 15:54:10
# title: EtCPC2022 - Practice - 7 / LogDB
# language: Python 3


a = []
d = {}
while 1:
    s = input()
    if s == '':
        break
    s = s.replace(' ', '')
    b = s.strip().split(')')
    for i in b:
        if i == '':
            continue
        x,y = i.strip().split('(')
        y = y.strip().split(',')
        z = []
        for j in y:
            z.append(j.strip())
        if x in d:
            d[x].append(z)
        else:
            d[x] = [z]
while 1:
    try:
        s = input().replace(' ', '').strip()[:-1]
        x,y = s.split('(')
        y = y.split(',')
        z = []
        if not x in d:
            print(0)
            continue
        for i in d[x]:
            if len(y) == len(i):
                z.append(i)
        e = {}
        idx = -1
        
        
        for i in y:
            idx += 1
            if i == '_':
                continue
            elif i[0] != '_':
                q = []
                for k, j in enumerate(z):
                    if j[idx] != i:
                        q.append(k)
                q.reverse()
                for j in q:
                    z.pop(j)
            if i in e:
                e[i].append(idx)
            else:
                e[i] = [idx]
        ans = len(z)
        #print(x, z)
        m = []
        for i in e:
            if len(e[i]) == 1:
                continue
            m.append(e[i])
        for j in z:
            c = False
            for i in m:
                s = set()
                for k in i:
                    s.add(j[k])
                if len(s) > 1:
                    break
            else:
                c = True
            if(c == False):
                ans -= 1
        print(ans)
                
            
    except EOFError:
        break

