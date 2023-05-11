# https://open.kattis.com/problems/shopaholic
# Time: 2022-09-01 22:50:44
# title: Shopaholic
# language: Python 3


n = int(input())
a = list(map(int, input().split()))
b = 0
a.sort(reverse=True)
for i in range(2, n, 3):
    b += a[i]
print(b)