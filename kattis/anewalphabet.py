# https://open.kattis.com/problems/anewalphabet
# Time: 2022-08-15 09:49:48
# title: A New Alphabet
# language: Python 3


a = [
    '@',
    '8',
    '(',
    '|)',
    '3',
    '#',
    '6',
    '[-]',
    '|',
    '_|',
    '|<',
    '1',
    '[]\/[]',
    '[]\[]',
    '0',
    '|D',
    '(,)',
    '|Z',
    '$',
    "']['",
    '|_|',
    '\/',
    '\/\/',
    '}{',
    "`/",
    '2'
    
    
    ]
s = input().lower()
b = ''
for i in s:
    if not(97 <= ord(i) <= 123):
        b += i
    else:
        b += a[ord(i)-97]
print(b)
