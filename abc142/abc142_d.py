import numpy as np

def gcd(m, n):
    x=max(m, n)
    y=min(m, n)
    if x%y == 0:
        return y
    else:
        z=x%y
        while x%y != 0:
            z=x%y
            x=y
            y=z
        
        return int(z)
def lcm(x, y):
    return (x * y) // gcd(x, y)

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if int(gcd(n, k)) == 1:
            amount += 1
    return amount

def cd(x,y):
    cd=[]
    cd.append(1)
    for i in range(2, min(x,y)+1):
        if x % i == 0 and y % i == 0:
            cd.append(i)
    return cd

A, B = map(int, input().split())
gcd = gcd(A, B)
cd = cd(A, B)
for i in cd:
    print(phi(i))

print(gcd)


'''

'''