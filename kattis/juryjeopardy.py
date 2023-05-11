# https://open.kattis.com/problems/juryjeopardy
# Time: 2022-09-03 21:53:21
# title: Jury Jeopardy
# language: Python 3


n = int(input())
m = [(0, 1), (-1, 0), (0, -1), (1, 0)]
print(n)
for _ in range(n):
    s = input()
    a = [['#' for i in range(202)]for j in range(202)]
    x = 100
    y = 0
    d = 0
    a[x][y] = '.'
    u1 = 10000
    u2 = 100
    h = 0
    for i in s:
        if i == 'F':
            pass
        elif i == 'B':
            d = (d+2)%4
        elif i == 'R':
            d = (d-1)%4
        else:
            d = (d+1)%4
        u, v = m[d]
        x += u
        y += v
        a[x][y] = '.'
        h = max(h, y)
        u1 = min(u1, x)
        u2 = max(u2, x)
        #print(x, y)
    print(u2-u1+3, h+2)
    for i in range(u1-1, u2+2):
        print(''.join(a[i][:h+2]))
        
