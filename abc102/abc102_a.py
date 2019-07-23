N = int(input())

for i in range(N, (N+1)*100, N):
    if i % 2 == 0 and i % N == 0:
        break

print(i)


'''
3
6

10
10

999999999
1999999998
'''