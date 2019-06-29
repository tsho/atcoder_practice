import numpy as np
import itertools
import math
import math

def comb(n, r):
    return  (math.factorial(n) // math.factorial(r) // math.factorial(n - r))

d, k = map(int, input().split())
r=d-k
ans=[]
seq = []

cnst = 1000000000+7
for i in range(1, k+1):
    if (r+1) != i:
#        ans = comb(r+1, i) * i
        ans = comb(d-k+1, i) * comb(k-1, i-1)
    else:
        ans = 1
    print(int(ans)%cnst)

#print(half, d_sorted)

'''
a < k < N < 2000
10*9 + 7

5 3
3
6
1


2000 3
1998
3990006
327341989





'''


