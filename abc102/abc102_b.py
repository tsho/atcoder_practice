N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i, N):
        ans = max(ans, abs(A[i] - A[j]))

print(ans)

'''
https://atcoder.jp/contests/abc102/tasks/abc102_b
4
1 4 6 3
5

2
1000000000 1
999999999

5
1 1 1 1 1
0
'''