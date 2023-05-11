# https://open.kattis.com/problems/fruitbaskets
# Time: 2022-09-10 15:35:00
# title: Fruit Baskets
# language: Python 3


n = int(input())
a = list(map(int, input().split()))
b = sum(a) * pow(2, n-1)

from itertools import combinations
c = [combinations(a, i) for i in range(1, 4)]
d = []
for i in list(c):
    d.extend(i)
for i in d:
    if sum(i) < 200:
        b -= sum(i)
print(b)