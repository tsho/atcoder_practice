import numpy as np
N, M = map(int, input().split())

A = list(map(int, input().split()))
for i in range(M):
    B, C = map(int, input().split())
    A.sort()
    print("sort = ", A)

    A = [ C if (j < C and k<B) else j for k, j in enumerate(A)]
#    [f(x) if condition else g(x) for x in sequence]
    print(A)

print(sum(A))




'''if int(min(R) - max(L) + 1) < 0:
    print(0)
else:
    print(int(min(R) - max(L) + 1))

#print(len(cards) - np.sum(cards) )
#print(int(len(cards)-np.sum(cards)) )

N M
A1 AN
B1 C1
B2 C2
...
BN CN

3 2
5 1 4
2 3
1 5

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