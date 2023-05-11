# https://open.kattis.com/problems/smartphone
# Time: 2022-09-05 21:53:37
# title: Smart Phone
# language: Python 3


def z(x, y):
    k = 1
    i = 0
    while i < len(x) and i < len(y) and x[i] == y[i]:
        i += 1
    k += len(y) - i + len(x) - i
    return k
    
for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    m = 10000
    m = min(m, z(a, b) - 1)
    m = min(m, z(a, c))
    m = min(m, z(a, d))
    m = min(m, z(a, e))
    print(m)