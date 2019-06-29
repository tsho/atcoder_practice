import numpy as np

n = int(input())
p = []
p = list(map(int, input().split()))
print(p)

cnt=0
for i in range(1, n-1):
    tmp = np.array([p[i-1], p[i], p[i+1]])
#    print(np.argsort(tmp))
#    print(np.argsort(tmp)[0], np.argsort(tmp)[1], np.argsort(tmp)[2])
    if np.argsort(tmp)[1] == 1:
        cnt+=1

print(cnt)

'''
ASSA

'''