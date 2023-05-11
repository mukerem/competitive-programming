# https://open.kattis.com/problems/colourwars
# Time: 2022-09-10 16:13:41
# title: Colour Wars
# language: Python 3


from math import ceil
n = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
s = 0
for i in b:
    j = b[i]
    k = int(ceil(j / (i+1)))
    s += (i+1) * k
print(s)