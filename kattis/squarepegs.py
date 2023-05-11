# https://open.kattis.com/problems/squarepegs
# Time: 2022-09-09 21:10:29
# title: Square Peg in a Round Hole
# language: Python 3


n,m,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = b[:]
for i in c:
    d.append(i / (2**0.5))
d.sort(reverse=True)
a.sort(reverse=True)
v = [False for i in range(n)]
h = 0
for i in d:
    for j in range(n):
        if i < a[j] and v[j] == False:
            v[j] = True
            h += 1
            break
print(h)