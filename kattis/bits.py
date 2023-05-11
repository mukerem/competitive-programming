# https://open.kattis.com/problems/bits
# Time: 2022-09-08 22:32:58
# title: Bits
# language: Python 3


for _ in range(int(input())):
    c = input()
    m = 0
    for i in range(1, len(c)+1):
        f = int(c[:i])
        f = bin(f)[2:]
        m = max(m, f.count('1'))
    print(m)