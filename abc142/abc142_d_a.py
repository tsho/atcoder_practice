# Ref:https://atcoder.jp/contests/abc142/submissions/7742797

def prime_factorize(N):
    exponent = 0
    while N%2 == 0:
        exponent += 1
        N //= 2
    if exponent: factorization = [[2,exponent]]
    else: factorization = []
    i=1
    while i*i <=N:
        i += 2
        if N%i: continue
        exponent = 0
        while N%i == 0:
            exponent += 1
            N //= i
        factorization.append([i,exponent])
    if N!= 1: factorization.append([N,1])
    assert N != 0, "zero"
    return factorization
    
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline 
from fractions import gcd

a,b = [int(i) for i in readline().split()]

g = gcd(a,b)

if g == 1:
    print(1)
else:
    l = prime_factorize(g)
    print(len(l)+1)



