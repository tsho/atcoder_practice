A = list(map(int, input().split()))

cost = []
cost.append(abs(A[0] - A[1]))
cost.append(abs(A[1] - A[2]))
cost.append(abs(A[2] - A[0]))
cost.remove(max(cost))

print(sum(cost))

'''
https://atcoder.jp/contests/abc103/tasks/abc103_a
1 6 3
5

11 5 5
6

100 100 100
0
'''