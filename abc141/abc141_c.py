N, K, Q = map(int, input().split())

P = [0] * N
for i in range(Q):
    tmp = int(input()) - 1
    P[tmp] += 1

sumP = sum(P)
for n in range(N):
    ans = 'No'
    total = sumP - P[n]
    if  K - total > 0:
        ans = 'Yes'
    print(ans)


'''
6 3 4
3
1
3
2
No
No
Yes
No
No
No




6 5 4
3
1
3
2
Yes
Yes
Yes
Yes
Yes
Yes


10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9
No
No
No
No
Yes
No
No
No
Yes
No




'''
