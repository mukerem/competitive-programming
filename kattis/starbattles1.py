# https://open.kattis.com/problems/starbattles1
# Time: 2022-09-16 22:33:15
# title: Star Battles I
# language: Python 3


a = []
for i in range(10):
    s = list(map(int, list(input())))
    a.append(s)
    
b = []
for i in range(10):
    b.append(list(input()))

def check():
    for i in range(10):
        if b[i].count('*') != 2:
            return False
    for i in range(10):
        c = []
        for j in range(10):
            c.append(b[j][i])
        if c.count('*') != 2:
            return False
    d = {i: [] for i in range(10)}
    for i in range(10):
        for j in range(10):
            d[a[i][j]].append(b[i][j])
    for i in d:
        if d[i].count('*') != 2:
            return False
            
    for i in range(10):
        for j in range(9):
            if b[i][j] == '*' and b[i][j+1] == '*':
                return False
    
    for i in range(9):
        for j in range(10):
            if b[i][j] == '*' and b[i+1][j] == '*':
                return False
    for i in range(9):
        for j in range(9):
            if b[i][j] == '*' and b[i+1][j+1] == '*':
                return False
                
    for i in range(9):
        for j in range(1, 10):
            if b[i][j] == '*' and b[i+1][j-1] == '*':
                return False
                
    return True
    
if check():
    print('valid')
else:
    print('invalid')
            
        