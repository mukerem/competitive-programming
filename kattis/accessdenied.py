# https://open.kattis.com/problems/accessdenied
# Time: 2022-10-08 19:19:44
# title: Access Denied
# language: Python 3


c = False
p = 0
import string
a = string.ascii_uppercase + string.ascii_lowercase +  string.digits
password = ['A']
u = -1
idx = 0
while 1:
    print(''.join(password), flush=True)
    s = input()
    if s == "ACCESS GRANTED":
        break
    if s == "ACCESS DENIED (5 ms)":
        password.append('A')
        #print(p, flush=True)
        continue
    t = int(s[15:-4])
    t = (t-5)//9
    #print(t)
    if t == u:
        idx+=1
    else:
        u = t
        idx = 0
    password[t-1] = a[idx]
    
