# https://open.kattis.com/problems/guessinggame
# Time: 2022-09-16 16:45:49
# title: Guessing Game
# language: Python 3


a = [30]
b = [0]
while 1:
    x = int(input())
    if x == 0:
        break
    y = input()
    if y == 'right on':
        if max(b) < x < min(a):
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        a = [30]
        b = [0]
    elif y == 'too high':
        a.append(x)
    elif y == 'too low':
        b.append(x)