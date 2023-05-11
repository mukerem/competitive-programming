# https://open.kattis.com/problems/classy
# Time: 2022-10-08 20:58:34
# title: A Classy Problem
# language: Python 3


def change(x):
    u = ''.join(x)
    u=u.replace('upper', '0')
    u=u.replace('middle', '1')
    u=u.replace('lower', '2')
    u += (10-len(u)) * '1'
    return u

for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        x,y = input().split(':')
        z = y.strip().split()[0].split('-')[::-1]
        s.append((change(z), x))
    s.sort()
    
    for i,j in s:
        print(j)
    print("=" * 30)

