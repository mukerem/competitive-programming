# https://open.kattis.com/problems/4thought
# Time: 2019-11-20 22:18:46
# title: 4 thought
# language: Python 2


op = [' * ', ' + ', ' - ',' / ']
s = '4'
def thoughts(n):
    for i in op:
        for j in op:
            for k in op:
                x = s+i+s+j+s+k+s
                if eval(x) == n:
                    return x+" = "+str(n)
    return ""
for _ in range(int(input())):
    n = int(input())
    c = thoughts(n)
    if c:
        print(c)
    else:
        print('no solution')
            
