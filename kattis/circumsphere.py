# https://open.kattis.com/problems/circumsphere
# Time: 2022-09-08 22:03:31
# title: Circumsphere
# language: Python 3


a = []
b= []
for  i in range(4):
    x,y,z = map(float, input().split())
    a.append([x,y,z, -1])
    b.append((x*x+y*y+z*z)/2)
    

def determinant(c, total=0):
    K = len(c)
    if K == 2:
        return c[0][0] * c[1][1] - c[0][1]*c[1][0]

    for i in range(K):
        e = []
        for j in c[1:]:
            e.append(j[:])
        for j in e:
            j.pop(i)
        sign = (-1) ** (i % 2) 
        h = determinant(e)
        total += sign * c[0][i] * h 
 
    return total
det = determinant(a)

for i in range(3):
    e = []
    for j in a:
        e.append(j[:])
    idx = 0
    for j in e:
        j[i] = b[idx]
        idx += 1
    x = determinant(e)
    print(x/det, end= ' ')

