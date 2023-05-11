# https://open.kattis.com/problems/irepeatmyself
# Time: 2022-09-03 22:10:57
# title: I Repeat Myself I Repeat Myself I Repeat
# language: Python 3


for _ in range(int(input())):
    s = input()
    for i in range(1, len(s)+1):
        k = s[:i]
        #print(k)
        for j in range(0, len(s), i):
            z = s[j: j+i]
            #print(z)
            if len(z) < i:
                if not z == k[:len(z)]:
                    break
            elif not k == z:
                break
        else:
            print(i)
            break
            
