import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

a, b = na()

ans = 0
if (a > 0 and a < 10) and (b > 0 and b < 10):
    ans = a * b
else:
    ans = -1    

print(ans)
