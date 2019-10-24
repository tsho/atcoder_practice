import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

N = ni()
a = na()

ans = 0
for i in a:
    ans += i

print(ans)
