A, B, C = map(int, input().split())

ans = C - (A-B)
if ans < 0:
    ans = 0
print(ans)


'''
6 4 3

0 3
IMPOSSIBLE

998244353 99824435
549034394
'''