import time
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = time.time()
ans = []
for a in A:
    heapq.heappush(ans, -a)

for _ in range(M):
    l = heapq.heappop(ans)
    heapq.heappush(ans, -((-l)//2) )

print(-sum(ans))
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
