import sys
import math

stdin = sys.stdin

na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

N, a, b = na()

mod = int(abs(b-a) % 2)
if mod == 0:
    print(int(abs(a-b)/2))
elif mod == 1:
    if a+b <= (N-a)+(N-b):
        print(max(a-1, b-1))
    elif a+b > (N-a)+(N-b):
        print(max(N-a, N-b))
