# https://open.kattis.com/problems/wordcloud
# Time: 2022-09-04 12:12:50
# title: Word Cloud
# language: Python 3


from math import ceil
q = 1
while 1:
    W, n = map(int, input().split())
    if W+n == 0:
        break
    a = []
    m = 0
    for i in range(n):
        x, y = input().split()
        y = int(y)
        a.append((x, y))
        m = max(m, y)
    h = 0
    x = []
    y = 0
    for w, c in a:
        p = 8 + int(ceil(40*(c-4)/(m-4)))
        width = int(ceil(9/16*len(w) * p))
        if y + width <= W:
            y += width + 10
            x.append(p)
        else:
            h += max(x)
            x = [p]
            y = width + 10
    if x:
        h += max(x)
    print(f'CLOUD {q}: {h}')
    q += 1
