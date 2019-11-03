import sys

def divisor(n):
    i = 1
    l = []
    while i * i <= n:
        if n%i == 0:
            l.append(i)
            l.append(n//i)
        i += 1
    l.sort()
    return l

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline()

N = ni()
ans = 0
if N > 1:
    div = divisor(N)
    #print(div, div[len(div)//2 - 1])
    if len(div) > 1:
        i = div[len(div)//2 - 1] - 1
        j = (N // (div[(len(div)//2) - 1]))  - 1
        ans = i + j
    else:
        ans = 1
elif N == 1:
    ans = 0
else:
    ans = 1

print(ans)


'''
10
5

50
13

10000000019
10000000018

100000000019

'''


