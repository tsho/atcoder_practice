n, k = map(int, input().split())
s = input()

ss = ''
for u, v in enumerate(s):
    if u == k-1:
        ss = ss + v.lower()
    else:
        ss = ss + v
print(ss)

'''
ex.1
3 1
ABC
'''