import math

A, B, C, D = map(int, input().split())
ans=0

def gcd(m, n):
    x=max(m, n)
    y=min(m, n)
    if x%y == 0:
        return y
    else:
        while x%y!=0:
            z=x%y
            x=y
            y=z
        else:
            return z

def lcm(x, y):
    return (x * y) // gcd(x, y)

def counter(x, A, B):
    Cx=0
    i=1
    cnt=0
    i=A//x
    Cx=x*i
#    print('first Cx', Cx)
    while Cx <= B:
#        print(Cx, i)
        cnt+=1
        i+=1
        Cx=x*i
    return cnt

lcmCD=lcm(C, D)
ans=B-A+1
print('total', ans)
ans-=((B//C) - ((A-1)//C))
print(ans)
print( "(B//C) - (A//C))", (B//C), (A//C), (B//C)-(A//C))
ans-=((B//D) - ((A-1)//D))
print(ans)
print( "(B//D) - (A//D))", (B//D), (A//D), (B//D)-(A//D))
ans+=((B//lcmCD) - ((A-1)//lcmCD))
print( "(lcm//D) - (lcm//D))", lcmCD, (B//lcmCD), (A//lcmCD), (B//lcmCD)-(A//lcmCD))
print(ans)

'''
4 5 6 7 8 9
2:  4 6 8

3:  6



for i in range(A, B+1):
    if i % C != 0:
        if i % D != 0:
            cnt+=1



4 9 2 3
2


10 40 6 8
23

314159265358979323 846264338327950288 419716939 937510582
532105071133627368
'''