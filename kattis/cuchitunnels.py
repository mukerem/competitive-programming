# https://open.kattis.com/problems/cuchitunnels
# Time: 2022-09-23 10:45:07
# title: Cu Chi Tunnels
# language: Python 3


n = int(input())
a = list(map(int, input().split()))
x = sum(a)

if x != 2 * n - 2 or a[0] == 0 or a[-1] != 1:
    print('NO')
elif a.count(1) == 0:
    print('NO')
else:
    s = a[0]
    for i in range(1, n):
        if (s <= 2*(i-1)):
            print('NO')
            break
        s += a[i]
        if s < 2*i:
            print('NO')
            break
    else:          
        print('YES')