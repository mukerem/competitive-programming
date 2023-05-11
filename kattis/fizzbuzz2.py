# https://open.kattis.com/problems/fizzbuzz2
# Time: 2022-09-18 21:03:25
# title: FizzBuzz
# language: Python 3


n, m = map(int, input().split())
a = []
for i in range(n):
    b = input().split()
    c = 0
    for j, v in enumerate(b):
        k = j + 1
        if k%3 == 0 and k%5 == 0:
            if v == 'fizzbuzz': c += 1
        elif k%3 == 0:
            if v == 'fizz': c += 1
        elif k%5 == 0:
            if v == 'buzz': c += 1
        else:
            if v == str(k): c += 1
    a.append((c, -i-1))
d, c = max(a)
print(-c)