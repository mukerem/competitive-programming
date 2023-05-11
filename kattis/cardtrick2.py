# https://open.kattis.com/problems/cardtrick2
# Time: 2020-11-26 14:55:26
# title: Card Trick
# language: Python 2


for i in range(input()):
    n = input()
    if n == 1:
        print 1
        continue
    a = [0] * n
    a[1] = 1
    c = 2
    index = 1
    while c <= n:
        j = 0
        while j<=c:
            index += 1
            index %= n
            
            if not a[index]:
                j += 1
                
        index %= n   
        a[index] = c
        c += 1
    for i in a:
        print i,
    print
