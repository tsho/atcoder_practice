from operator import itemgetter
import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=itemgetter(0))
q = []
idx = 0
ans = 0

for i in range(1, M+1):
    while idx < N:
        a, b = AB[idx]
        if a <= i:
            heapq.heappush(q, -b)
            idx += 1
        else:
            break
    if len(q)>0:
        b = heapq.heappop(q)
        ans -= b

print(ans)



'''
N, M = map(int, input().split())
A=[0]*N
B=[0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dy = 0
ans = 0
total_dy = 0
cnt = 0
while total_dy <= M:
    tmp_max = max(B)
    idxs = [i for i, x in enumerate(B) if x == max(B)]
    if len(idxs) > 1:
        for i in idxs:
            if cnt == 0:
                tmp_max_idx = i
                cnt += 1
            elif cnt > 0 and A[tmp_max_idx] < A[i]:
                tmp_max_idx = i
    else:
        tmp_max_idx = B.index(max(B))

    cnt = 0
    if A[tmp_max_idx]+dy <= M:
        ans += tmp_max
        total_dy = A[tmp_max_idx] + dy
        dy += 1

    A.pop(tmp_max_idx)
    B.pop(tmp_max_idx)
    tmp_max_idx = 0
    if A == [] or B ==[]:
        break
    print(A, B, ans, dy, total_dy)

print(ans)

#for i in range(N):
#    for j in range(i+1, N):




2 < N < 10**5
si < len(si) = 10


3 4
4 3
4 1
2 2
5


5 3
1 2
1 3
1 4
2 1
2 3
10

1 1
2 1
0


'''