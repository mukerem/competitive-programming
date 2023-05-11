# https://open.kattis.com/problems/klockan2
# Time: 2022-10-07 23:51:27
# title: The Clock
# language: Python 3


a = {}
n = int(input())
for i in range(12):
    for j in range(0,360,6):

        x = i*30 + (j/12)
        x = round(x*10)
        if x%5 in [0,1,2]:
            x -= x%5
        else:
            x -= x%5
            x += 5
        y = j*10
        z = (y-x)%3600
        a[z] = f'{str(i).zfill(2)}:{str(j//6).zfill(2)}'
print(a[n])
