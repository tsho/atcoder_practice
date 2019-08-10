K, X = map(int, input().split())

ans = []
for i in range(X - K + 1, X + K):
    if i > -1000000 or i < 1000000:
        ans.append(i)

print(" ".join(map(str, ans)))


'''
1 K 100
0 X 100

-1000000 < x < 1000000

3 7
5 6 7 8 9

4 0
-3 -2 -1 0 1 2 3
'''