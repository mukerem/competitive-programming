# https://open.kattis.com/problems/autori
# Time: 2019-08-18 19:58:04
# title: Autori
# language: Python 2


a = raw_input().split('-')
b = ''
for i in a:
    b += i[0]
print b
