# https://open.kattis.com/contests/uybefk
# Time: 2019-11-27 09:42:00
# title: CPC Wednesday #10 / Association for Computing Machinery
# language: Python 2


n,p = [int(i) for i in raw_input().split()]
x = [int(i) for i in raw_input().split()]

time = 0
ans = 0
tot = 0
if x[p] <= 300:
    time = x[p]
    ans = 1
    x.pop(p)
    x.sort()
    tot = time
    for i in x:
        tot += i
        if tot > 300:
            break
        ans += 1
        time += tot
print ans, time
    
    
