import math 
import numpy as np
from operator import itemgetter
name=[]
score=[]
N = int(input())
for i in range(N):
    print(i)
    tmp1, tmp2 = input().split()[0], input().split()[1]
    name.append(tmp1)
    score.append(tmp2)
    print(tmp1, tmp2)

print(name)
#List2=np.genfromtxt(List, dtype=None, names=["a", "b"])
#print(np.argsort(List2,axis=1))



'''
a = sorted(List, key=lambda x:(x[0],x[1])) #reverse=True)
for i in range(N):
    sp[i][0] = input().split()[0]
    sp[i][1] = int(input().split()[1])
    print(sp)
print(sp)    


List=[list(input().split()) for i in range(N)]
a = sorted(List, key=lambda x:(x[0],x[1])) #reverse=True)
for i, x in enumerate(List):
    print(a[i])



6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40


'''