# https://open.kattis.com/contests/uybefk
# Time: 2019-11-27 10:04:09
# title: CPC Wednesday #10 / Kafkaesque
# language: Python 2


n = input()
x = []
x.append(input())
ans = 1
for i in range(n-1):
    x.append(input())
    if x[-2] > x[-1]:
        ans += 1
print ans
