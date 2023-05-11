# https://open.kattis.com/problems/fromatob
# Time: 2022-09-07 19:31:39
# title: From A to B
# language: Python 3


n, m = map(int, input().split())
if m >= n:
    print(m-n)
else:
    c = 0
    while n > m:
        if n%2 == 0:
            n = n // 2
        else:
            n += 1
        c += 1
        
    print(c + m-n)