# https://open.kattis.com/contests/mx2edj
# Time: 2022-09-07 21:01:22
# title: EtCPC2022 - Practice - 4 / Deathstar
# language: Python 3


n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
ans = [[0 for i in range(64)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s = bin(a[i][j])[2:]
        k = len(s)
        idx = -1
        for z in range(k):
            if s[idx] == '1':
                ans[i][idx] = 1
                ans[j][idx] = 1
            idx -= 1
for i in range(n):
    s = ''.join(map(str, ans[i]))
    print(int(s, 2), end = ' ')