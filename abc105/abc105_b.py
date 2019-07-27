N = int(input())

cnt = 0
for i in range(1, N+1, 2):
    cntt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cntt += 1
    if cntt == 8:
        cnt += 1
print(cnt)

'''
https://atcoder.jp/contests/abc106/tasks/abc106_b

105
1

7
0
'''