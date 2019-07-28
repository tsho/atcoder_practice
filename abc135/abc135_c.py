N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
tmp = 0
for i in range(N):
    tmp_mon = max(A[i] - tmp, 0)
    killed_mon = min(A[i], tmp)
    cnt += min(B[i], tmp_mon) + killed_mon

    if B[i] > tmp_mon:
        tmp = B[i] - tmp_mon
    elif B[i] <= tmp_mon:
        tmp = 0
    print(i, A[i], B[i], tmp,  tmp_mon, cnt)
    
print(A[-1], tmp)
cnt += min(A[-1], tmp)

print(cnt)


'''
2
3 5 2
4 5
9

3
5 6 3 8
5 100 8
22

2
100 1 1
1 100
3
'''
