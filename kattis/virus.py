# https://open.kattis.com/contests/knzvpe
# Time: 2022-09-21 13:40:46
# title: EtCPC2022 - Practice - 10 / Virus Replication
# language: Python 3


a = input()
b = input()
n = min(len(a), len(b))
m = len(b)
def c(x, y):
    for i in range(n):
        if x[i] != y[i]:
            return i
    return n
    
u = c(a,b)
v = c(a[::-1], b[::-1])
v = min(v, n-u)
print(max(m-u-v, 0))