# https://open.kattis.com/problems/everywhere
# Time: 2019-08-19 19:29:06
# title: I've Been Everywhere, Man
# language: Python 2


a = input()
for i in range(a):
    n = input()
    s = set()
    for j in range(n):
        x = raw_input()
        s.add(x)
    print len(s)
    
