D, N = map(int, input().split())

start = 100 ** D
if N == 100:
    N += 1
print(start * N)

'''
0 5
5

1 11
1199

2 85
850000
'''