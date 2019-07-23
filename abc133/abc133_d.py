import numpy as np

n = int(input())
a = [int(i) for i in input().split()] 
a = np.array(a)
x = np.zeros(n)

x[0] = sum(a) - (2*(sum(a[1::2])))

for i in range(n-1):
    x[i+1] = 2*a[i] - x[i]

print(' '.join(map(str, map(int, x))))


'''
3
2 2 4
2x + 2y + 2z = sum(a)

#print(M)
#print(ans, ans.T, ans.reshape(-1,1))

'''