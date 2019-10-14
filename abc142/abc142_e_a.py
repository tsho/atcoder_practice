#Ref:https://atcoder.jp/contests/abc142/submissions/7747672

import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, m = na()
a = []
pts = []
for i in range(m):
    la, lb = na()
    a.append(la)
    pt = 0
    for x in na():
        pt |= 1<<x-1
    pts.append(pt)

price = [99999999999999999] * (1<<n)
for i in range(m):
    price[pts[i]] = min(price[pts[i]], a[i])

dp = [9999999999999999] * (1<<n)
dp[0] = 0
for i in range(1<<n):
    if price[i] <= 100000:
        for j in range(1<<n):
            dp[j|i] = min(dp[j|i], dp[j] + price[i])
if dp[(1<<n)-1] >= 100000000:
    print(-1)
else:
    print(dp[(1<<n)-1])
