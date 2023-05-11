# https://open.kattis.com/problems/simon
# Time: 2022-10-07 22:47:42
# title: Simon Says
# language: Python 3


for _ in range(int(input())):
    s = input().split()
    if s[:2] == ['simon', 'says']:
        print(' '.join(s[2:]))
    else:
        print()