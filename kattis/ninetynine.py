# https://open.kattis.com/problems/ninetynine
# Time: 2022-09-16 20:25:26
# title: Ninety-nine
# language: Python 3


n = 1
print(2)
while n < 99:
    n = int(input())
    if n % 3 == 1:
        n += 2
    else:
        n += 1
    print(n)
