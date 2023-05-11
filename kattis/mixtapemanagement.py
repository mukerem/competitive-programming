# https://open.kattis.com/problems/mixtapemanagement
# Time: 2022-09-13 08:48:30
# title: Mixtape Management
# language: Python 3


n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    b.append('1'*i)
k = 101
for i in range(n):
    b[i] = str(k) + b[i]
    k += 1
print(*b)