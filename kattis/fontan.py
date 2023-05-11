# https://open.kattis.com/problems/fontan
# Time: 2022-09-05 21:42:20
# title: Fountain
# language: Python 3



n, m = map(int, input().split())
a= []
for i in range(n):
    a.append(list(input()))
for i in range(n-1):
    b = []
    for j in range(m):
        if a[i][j] == 'V':
            if a[i+1][j] == '.':
                a[i+1][j] = 'V'
            k = j
            while k < m and a[i+1][k] == '#':
                if a[i][k] == '#':
                    break
                if a[i][k] == '.' or a[i][k] == 'V':
                    a[i][k] = 'V'
                    if a[i+1][k] == '.':
                        a[i+1][k] = 'V'
                    if k < m-1 and a[i][k+1] == '.':
                        a[i][k+1] = 'V'
                        if a[i+1][k+1] == '.':
                            a[i+1][k+1] = 'V'
                k += 1
            k = j
            while k >= 0 and a[i+1][k] == '#':
                if a[i][k] == '#':
                    break
                if a[i][k] == '.' or a[i][k] == 'V':
                    a[i][k] = 'V'
                    if a[i+1][k] == '.':
                        a[i+1][k] = 'V'
                    if k > 0 and a[i][k-1] == '.':
                        a[i][k-1] = 'V'
                        if a[i+1][k-1] == '.':
                            a[i+1][k-1] = 'V'
                k -= 1
for i in a:
    print(''.join(i))
                
