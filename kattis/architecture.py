# https://open.kattis.com/problems/architecture
# Time: 2022-09-09 11:06:26
# title: Architecture
# language: Python 3


r, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if max(a) == max(b):
    print('possible')
else:
    print('impossible')