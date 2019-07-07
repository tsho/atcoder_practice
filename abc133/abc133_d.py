import numpy as np

n = int(input())
a = [int(i) for i in input().split()] 
ans = np.array(a)
if np.all(ans=0):
    print(ans)
    exit()

s = (n,n)
M = np.matrix(np.zeros(s))
for i in range(n):
    vec = np.zeros(n)
    vec[i]=1/2
    if i == (n-1):
        vec[0]=1/2
    else:
        vec[i+1]=1/2
    M[i] = vec
ans = (np.linalg.inv(M)*(ans.reshape(-1,1)))
print(' '.join(map(str, map(int, ans.T.tolist()[0]))))

'''
3
2 2 4
2x + 2y + 2z = sum(a)

#print(M)
#print(ans, ans.T, ans.reshape(-1,1))

'''