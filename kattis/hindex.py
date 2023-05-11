# https://open.kattis.com/problems/hindex
# Time: 2022-09-18 13:22:06
# title: H-Index
# language: Python 3


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
m = 0
for i, v in enumerate(a):
    if v >= i+1:
        m = i+1
    else:
        break
print(m)