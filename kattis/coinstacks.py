# https://open.kattis.com/problems/coinstacks
# Time: 2022-09-23 09:42:55
# title: Coin Stacks
# language: Python 3


n = int(input())
a = list(map(int, input().split()))
# a.sort()
x = sum(a)
def choose():
    m = max(a)
    idx = a.index(m)
    q = 0
    idx2 = 0
    for i in range(n):
        if i == idx:
            continue
        if a[i] > q:
            q = a[i]
            idx2 = i
    return idx, idx2
    
if x%2 == 1:
    print('no')
else:
    y = max(a)
    z = x-y
    if z >= y:
        print('yes')
        for i in range(x//2):
            i,j = choose()
            a[i] -= 1
            a[j] -= 1
            print(min(i,j)+1, max(i, j)+1)
    else:
        print('no')