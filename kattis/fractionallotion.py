# https://open.kattis.com/problems/fractionallotion
# Time: 2022-09-10 21:13:51
# title: Fractional Lotion
# language: Python 3


while 1:
    try:
        _, n = input().split('/')
        n = int(n)
        n = n*n
        x = 1
        count = 1
        while x*x<n:
            if n%x == 0:
                count += 1
            x += 1
        print(count)
    except EOFError:
        break
