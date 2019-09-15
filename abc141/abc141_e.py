import numpy as np
import time

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = time.time()

#np_A = np.array(A)
a_dic = {}
for i, a in enumerate(A):
    a_dic[i-1] = a

for m in range(M):
#    tmp = np_A.argmax()
#    np_A[tmp] = np_A[tmp] / 2

    max_a = max(a_dic, key=a_dic.get)
    a_dic[max_a] = a_dic[max_a]/2

print(sum(a_dic))
#print(sum(np_A))
print("elapsed_time:{0}".format(time.time() - start) + "[sec]")

'''
3 3
2 13 8
9

4 4
1 9 3 5
6


1 100000
1000000000
0

10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000


'''
