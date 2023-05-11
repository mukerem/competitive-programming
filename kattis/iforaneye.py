# https://open.kattis.com/problems/iforaneye
# Time: 2022-09-07 21:26:57
# title: An I for an Eye
# language: Python 3



x = {'at': '@', 'and': '&', 'won': '1', 'one': '1', 'two': '2',
     'too': '2', 'to': '2', 'four': '4', 'for': '4', 'bee': 'b',
     'bea': 'b', 'be': 'b', 'see': 'c', 'sea': 'c', 'eye': 'i',
     'owe': 'o', 'oh': 'o', 'are': 'r', 'you': 'u', 'why': 'y',
     'At': '@', 'And': '&', 'Won': '1', 'One': '1',  'Two': '2', 
     'Too': '2', 'To': '2', 'Four': '4', 'For': '4', 'Bee': 'B', 
     'Bea': 'B', 'Be': 'B', 'See': 'C', 'Sea': 'C',  'Eye': 'I', 
     'Owe': 'O', 'Oh': 'O', 'Are': 'R', 'You': 'U',  'Why': 'Y', 
     }


for _ in range(int(input())):
    t = input()
    i = 0
    while i < len(t):
        for j in range(4,1,-1):
            
            if t[i: i+j].lower() in x:
                z = t[i] + t[i+1: i+j].lower()
                t = t[:i] + x[z] + t[i+j:]
                break
        i += 1
    print(t)
        