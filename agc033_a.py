import numpy as np

ij = list(map(int, input().split()))
cor_n = np.zeros((ij[1],ij[0]), dtype = 'int8')
for y in range(ij[0]):
    index = [u for u, v in enumerate(str(input())) if v == '#']
    if index != []:
        #print(index)
        for x in index:
            cor_n[y, x] = 1
            print(x,y)
#print(cor_n, len(cor_n))
cnt=0

while(np.any(cor_n == 0) ):
    for u in list(zip(np.where(cor_n == 1)[0], np.where(cor_n == 1)[1])):
        if (u[0] - 1 >= 0):
            cor_n[u[0]-1, u[1]] = 1
        if (u[0] + 1 < ij[1]):
            cor_n[u[0]+1, u[1]] = 1
        if (u[1] + 1 < ij[0]):
            cor_n[u[0], u[1]+1] = 1
        if (u[1] - 1 >= 0):
            cor_n[u[0], u[1]-1] = 1
    #print(cor_n)
    cnt+=1
#    print(cnt)
print(cnt)
