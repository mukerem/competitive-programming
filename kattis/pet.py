# https://open.kattis.com/problems/pet
# Time: 2019-08-19 18:25:35
# title: Pet
# language: Python 2


a = []
for i in range(5):
    x = [int(j) for j in raw_input().split()]
    a.append(sum(x))
ma = max(a)
print a.index(ma) + 1, ma
