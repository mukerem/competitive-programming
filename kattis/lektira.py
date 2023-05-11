# https://open.kattis.com/problems/lektira
# Time: 2022-09-10 15:42:14
# title: Lektira
# language: Python 3


s = input()
n = len(s)
h = []
for i in range(1, n):
    for j in range(i+1, n):
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            d = a[::-1]+b[::-1]+c[::-1]
            h.append(d)
print(min(h))