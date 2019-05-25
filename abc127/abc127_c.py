import numpy as np
N, M = map(int, input().split())

L = np.zeros(M)
R = np.zeros(M)
for j in range(M):
    L[j], R[j] = map(int, input().split())

if int(min(R) - max(L) + 1) < 0:
    print(0)
else:
    print(int(min(R) - max(L) + 1))

#print(len(cards) - np.sum(cards) )
#print(int(len(cards)-np.sum(cards)) )

'''
N M
L1 R1
L2 R2
LM RM

4 2
1 3
2 4
2

10 3
3 6
5 7
6 9


100000 1
1 100000
100000


100000 2
1 100000
2 100000


import numpy as np
N, M = map(int, input().split())

cards = np.zeros(N) 
for j in range(M):
    L, R = map(int, input().split())
    for i in range(1, N+1):
        if cards[i-1] != 1:
            if L > i or R < i:
                cards[i-1] = 1
#        print("cards = ", cards, i, L, R)
        

#print(len(cards) - np.sum(cards) )
print(int(len(cards)-np.sum(cards)) )

'''