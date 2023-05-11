# https://open.kattis.com/problems/softpasswords
# Time: 2022-09-08 22:56:33
# title: Soft Passwords
# language: Python 3


s = input()
p = input()

if p == s or s[1:] == p and s[0].isdigit() or\
    s[:-1] == p and s[-1].isdigit():
        print('Yes')
else:
    d = ''
    for i in s:
        if i.islower():
            d += i.upper()
        else:
            d += i.lower()
    if d == p:
        print('Yes')
    else:
        print('No')
