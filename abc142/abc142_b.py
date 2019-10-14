n, k = (int(_) for _ in input().split())
h = list(map(int, input().split()))

cnt=0
for i in h:
    if i >= k:
        cnt += 1
print(cnt)
'''
4 150
150 140 100 200
'''
