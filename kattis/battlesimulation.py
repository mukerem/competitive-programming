# https://open.kattis.com/problems/battlesimulation
# Time: 2022-09-16 17:11:55
# title: Battle Simulation
# language: Python 3


s = input()
a = {
    'R': 'S',
    'B': 'K',
    'L': 'H'
}
x = ['RBL', 'RLB', 'BRL', 'BLR', 'LRB', 'LBR']
n = len(s)
i = 0
c = []
while i<n:
    if s[i: i+3] in x:
        c.append('C')
        i += 3
    else:
        c.append(a[s[i]])
        i += 1
print(''.join(c))