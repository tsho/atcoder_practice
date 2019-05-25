import math
n, k = map(int, input().split())

sum = 0.0000

for i in range(1, n+1):
    if k-1 < i:
        break
    else:
       
#    if i % 100 == 0:
#        print('i =', i, 'k = ', k, 'k / i = ', float(k)/i, x, (1/n) * ((0.5)**x) )
        sum = sum + ((0.5)**(math.log2(k/i)))
#    print('x =', ( (1/n) * (0.5)**x ))


print(sum/n)

'''
3 10
0.145833333333


100000 5
0.999973749998


from math import log2
n,k=map(float,input().split())
ans=0
for i in range(1,int(n+1)):
    if k>=i:
        ans=ans+0.5**-(-log2(k/i)//1)
    else:
        ans=ans+1
ans=ans/n
print(ans)
from math import log2
n,k=map(float,input().split())
ans=0
for i in range(1,int(n+1)):
    if k>=i:
        ans=ans+0.5**-(-log2(k/i)//1)
    else:
        ans=ans+1
ans=ans/n
print(ans)
提出情報

'''




