s = input()
a = int(s[:2]); b = int(s[2:])

def check_mm(n):
    if  0 < n and n < 13:
        return True
    else:
        return False

if a == 0 or b == 0:
    print('NA')
elif check_mm(a) and check_mm(b):
    print('AMBIGUOUS')
elif check_mm(b):
    print('YYMM')
elif check_mm(a):
    print('MMYY')








'''
n, k = map(int, input().split())
s = input()

ss = ''
for u, v in enumerate(s):
    if u == k-1:
        ss = ss + v.lower()
    else:
        ss = ss + v
print(ss)


print('YYMM')
print('MMYY')
print('AMBIGUOUS')
print('NA')


ex.1
3 1
ABC

ex.1
1905
YYMM

ex.2
0112
AMBIGUOUS

ex.3
1700
NA
'''
