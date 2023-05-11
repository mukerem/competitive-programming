# https://open.kattis.com/problems/alphabet
# Time: 2022-09-18 22:17:30
# title: Alphabet
# language: Python 3


def lis(arr):
    n = len(arr)
    lis = [1]*n
 
    for i in range (1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum
s=input()
arr = []
for i in s:
    arr.append(ord(i)-97)
m= lis(arr)
print(26-m)