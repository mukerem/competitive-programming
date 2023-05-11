# https://open.kattis.com/problems/wordsfornumbers
# Time: 2022-09-08 23:16:46
# title: Words for Numbers
# language: Python 3


def word(n):
    w = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

    if n in w:
        return w[n]
    else:
        return w[n-n%10] + '-' + w[n%10].lower()
while 1:
    try:
        s = input().split()
        idx = 0
        for i in s:
            if i.isdigit():
                q = word(int(i))
                if idx == 0:
                    q = q.capitalize()
                else:
                    q = q.lower()
                print(q, end = ' ')
            else:
                print(i, end= ' ')
            idx += 1
        print()
    except EOFError:
        break
