# https://open.kattis.com/problems/textureanalysis
# Time: 2022-09-09 20:03:38
# title: Texture Analysis
# language: Python 3


k = 1
while 1:
    s = input()
    if s == 'END':
        break
    a = []
    for i in range(len(s)):
        if s[i] == '*':
            a.append(i)
    b = []
    for i in range(len(a)-1):
        b.append(a[i+1] - a[i])
    c = set(b)
    if len(c) <= 1:
        print(k, 'EVEN')
    else:
        print(k, 'NOT EVEN')
    k += 1