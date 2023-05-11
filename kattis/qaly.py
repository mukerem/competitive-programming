# https://open.kattis.com/problems/qaly
# Time: 2019-08-19 17:16:39
# title: Quality-Adjusted Life-Year
# language: Python 2


a = input()
sum = 0
for i in range(a):
    x , y =[float(k) for k in raw_input().split()]
    sum += x*y
print "%.3f"%sum
