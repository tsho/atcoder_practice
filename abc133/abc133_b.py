import math
N, D = map(int, input().split())
#x=[0]*D
x=[]
for j in range(N):
    x.append([int(i) for i in input().split()])

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        d = 0
        for k in range(D):
            d += (x[i][k] - x[j][k])**2
#        print(d, i, j, math.sqrt(d).is_integer(), math.sqrt(d).is_integer())
        if math.sqrt(d).is_integer():
            cnt += 1

print(cnt)
