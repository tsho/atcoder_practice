

## D
### sample1
https://atcoder.jp/contests/abc130/submissions/5964024

- hitstalesさん


```
import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
 
def main():
    N, K = LI()
    A = LI()
    acc = 0
    ans = 0
    j = 0
    for i in range(N):
        acc += A[i]
        while acc >= K:
            ans += (N - i)
            acc -= A[j]
            j += 1
    return ans
 
print(main())
```


### sample2
- iehnさん
- Yellow
https://atcoder.jp/contests/abc130/submissions/5957825
```
import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def main():
    n,k = LI()
    a = LI()
    l = 0
    t = 0
    r = 0
    for i in range(n):
        t += a[i]
        while t >= k:
            t -= a[l]
            l += 1
        r += l

    return r


print(main())
```




## sample3
- nagissさん
- Blue
https://atcoder.jp/contests/abc130/submissions/5959826
```
N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
ans = 0
l = 0
for r, a in enumerate(A):
    s += a
    while l < N:
        al = A[l]
        if s-al >= K:
            l+=1
            s-=al
        else:
            break
    if s>=K:
        ans += l+1
print(ans)
```

## sample4
- yaketake08さん
- yellow

https://atcoder.jp/contests/abc130/submissions/5960096
```
N, K = map(int, input().split())
*A, = map(int, input().split())

s = 0; q = 0
res = 0
for p in range(N):
    while q < N and s + A[q] < K:
        s += A[q]
        q += 1
    res += q - p
    if p < q:
        s -= A[p]
    else:
        q = p+1
print((N+1)*N//2 - res)
```
