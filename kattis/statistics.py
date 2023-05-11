# https://open.kattis.com/contests/qena3v
# Time: 2020-12-12 14:07:16
# title: Day 6 Afternoon / Statistics
# language: Python 2


case = 1
while 1:
    try:
        n = [int(i) for i in raw_input().split()]
        x = n[1:]
        print ("Case %d: %d %d %d" % (case, min(x), max(x), max(x) - min(x)))
        case += 1
    except EOFError:
        break
