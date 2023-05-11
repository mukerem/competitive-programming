# https://open.kattis.com/problems/signprofile
# Time: 2022-09-15 22:51:39
# title: Sign Profile
# language: Python 3



from math import sqrt 
def fun(a,b,c,d, x):
    z = a*x**3 + b*x**2 + c*x + d
    if z>0 and abs(z) > 1e-6:
        return 1
        
    if z<0 and abs(z) > 1e-6:
        return -1
        
while 1:
        d,c,b,a = map(float, input().split())
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        if a == 0 and b == 0 and c == 0:
            if d>0:
                print('+')
            elif d<0:
                print('-')
            continue
        u, v = a, b
        ans = []
        z = fun(a,b,c,d, -1000000000)
        ans.append(z)
        
        
        a = 3*a
        b = 2*b
        if a:
            if b*b - 4*a*c >= 0:
                x1 = (-b - sqrt(b*b - 4*a*c)) / (2*a)
                x2 = (-b + sqrt(b*b - 4*a*c)) / (2*a)
                if x1>x2: x1,x2=x2,x1
                z = fun(u,v,c,d, x1)
                ans.append(z)

                if x1 != x2:
                    z = fun(u,v,c,d, x2)
                    ans.append(z)
        elif b:
            x = -c / b
            z = fun(u,v,c,d, x)
            ans.append(z)

        z = fun(u,v,c,d, 1000000000)
        ans.append(z)
        
        q = []
        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                q.append(ans[i])
        q.append(ans[-1])
        for i in q:
            print(['+','-'][i==-1], end='')
        print()
    