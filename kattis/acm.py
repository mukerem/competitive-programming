# https://open.kattis.com/contests/uybefk
# Time: 2019-11-27 09:27:51
# title: CPC Wednesday #10 / ACM Contest Scoring
# language: Python 2


ans = 0
pen = 0

d = {}
che = {}
while True:
        x = raw_input()
        if x == '-1':
            break
        t,p, a = x.split()
        t = int(t)
        if p in d:
            if che[p]:
                continue
            if a == 'right':
                ans += 1
                pen += 20 * d[p] + t
                che[p]=1
            else:
                d[p] += 1
                che[p]=0
        else:
            if a == 'right':
                ans += 1
                pen += t
                che[p]=1
            else:
                d[p] = 1
                che[p]= 0
print ans, pen
