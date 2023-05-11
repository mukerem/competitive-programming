# https://open.kattis.com/problems/password
# Time: 2022-08-30 11:57:19
# title: Password Hacking
# language: Python 3


a = []
n = int(input())
for i in range(n):
    x, y = input().split()
    a.append(float(y))
b = []
a.sort(reverse=True)
t = 0
k = 0
for i, v in enumerate(a):
    t += v
    k += v * (i+1)
    #print(t)
print(k)
