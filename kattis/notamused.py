# https://open.kattis.com/problems/notamused
# Time: 2022-09-03 08:43:10
# title: Not Amused
# language: Python 3


day = 1
while 1:
    try:
        a = {}
        while 1:
            x = input()
            if x == 'CLOSE':
                break
            if x == 'OPEN':
                continue
            x,y,z = x.split()
            z = int(z)
            if x == 'ENTER':
                if y in a:
                    a[y] -= z
                else:
                    a[y] = -z
            else:
                if y in a:
                    a[y] += z
                else:
                    a[y] = z
        a = list(a.items())
        a.sort()
        print(f'Day {day}')
        for name, price in a:
            print(f'{name} $%.2f' % (price / 10))
        print()
        day += 1
                
    except:
        break