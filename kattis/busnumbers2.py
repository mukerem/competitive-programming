# https://open.kattis.com/problems/busnumbers2
# Time: 2022-09-07 19:25:43
# title: Bus Numbers
# language: Python 3


a = []
m = int(input())
def ramanujan():
    a = {}
    for i in range(1, 80):
        for j in range(i+1, 80):
            k = i**3 + j ** 3 
            if k > m:
                continue
            if k in a:
                a[k] += 1
            else:
                a[k] = 1
    b = [i for i in a if a[i] > 1]
    if b:
        print(max(b))
    else:
        print('none')
ramanujan()
            
