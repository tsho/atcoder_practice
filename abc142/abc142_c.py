import numpy as np

def gcd_k(m, n, k=0):
    x=max(m, n)
    y=min(m, n)
    if x%y == 0:
        return y
    else:
        z=x%y
        while x%y != 0 and z != k:
            z=x%y
            x=y
            y=z
        
        return z

def lcm(x, y):
    return (x * y) // gcd(x, y)

def cd(x,y):
    cd=[]
    cd.append(1)
    for i in range(2,min(x,y)+1):
        if x % i == 0 and y % i == 0:
            cd.append(i)
    return cd

A, B = map(int, input().split())
print(gcd_k(A, B))

'''

'''