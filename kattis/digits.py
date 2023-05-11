# https://open.kattis.com/problems/digits
# Time: 2022-09-27 08:20:52
# title: Digits
# language: Python 3


while 1:
    a = input()
    if a == 'END':
        break
    n = len(a)
    if n == 1:
        if a == '1':
            print(1)
        else:
            print(2)
    elif n<10:
        print(3)
    else:
        print(4)
