# https://open.kattis.com/problems/rsamistake
# Time: 2022-09-20 22:23:04
# title: RSA Mistake
# language: Python 3


a, b = map(int, input().split())
from math import isqrt
def is_prime(n):
    s = isqrt(n)
    for i in range(2, s+1):
        if n%i == 0:
            return False
    return True
    

if a == b:
    print('no credit')
elif is_prime(a) and is_prime(b):
    print('full credit')
else:
    u = {}
    v = {}
    q = 0
    while a%2 == 0:
        a //= 2
        q += 1
    if q:
        u[2] = q
    i = 3
    while i*i <= a:
        q = 0
        while a%i == 0:
            a //= i
            q += 1
        if q:
            u[i] = q
        i+= 2
    if a>1:
        u[a] = 1
        
    q = 0
    while b%2 == 0:
        b //= 2
        q += 1
    if q:
        v[2] = q
    i = 3
    while i*i <= b:
        q = 0
        while b%i == 0:
            b //= i
            q += 1
        if q:
            v[i] = q
        i+= 2
    if b>1:
        v[b] = 1
    for i in v:
        if i in u:
            u[i] += v[i]
        else:
            u[i] = v[i]
    for i in u:
        if u[i] >= 2:
            print('no credit')
            break
    else:
        print('partial credit')