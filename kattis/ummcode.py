# https://open.kattis.com/problems/ummcode
# Time: 2022-09-26 21:53:32
# title: Umm Code
# language: Python 3


a = input().split()
b = ''
import string
d = string.digits + string.ascii_lowercase +  string.ascii_uppercase
d = d.replace('u', '').replace('m', '')
for i in a:
    if len(i) == i.count('u') + i.count('m'):
        b += i
        continue
    c = i
    #c = c.replace('u', '').replace('m', '')
    for j in c:
        if j in d:
            break
    else:
        for j in c:
            if j in 'um':
                b += j
k = b.replace('u', '1').replace('m', '0')
f = ''
for i in range(0, len(k), 7):
    h = k[i: i+7]
    f += chr(int(h, 2))
print(f)
