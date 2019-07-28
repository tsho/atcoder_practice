A, B = map(int, input().split())

if not ((A + B) / 2.0).is_integer():
    print('IMPOSSIBLE')
else:
    print(int((A + B) / 2))


'''
2 16
9

0 3
IMPOSSIBLE

998244353 99824435
549034394
'''