import time
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
start = time.time()

a_dic = {}
for i, a in enumerate(A):
    a_dic[i] = a

for m in range(M):
    max_a = max(a_dic, key=a_dic.get)
    a_dic[max_a] = a_dic[max_a] // 2
#    print(a_dic[max_a])

#print(a_dic)

ans = sum(a_dic.values())
if ans < 0:
    ans = 0
print(ans)
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
