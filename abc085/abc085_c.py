import sys

stdin = sys.stdin

na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

N, Y = na()

ans="-1 -1 -1"
for i in range(N+1):
    if (i * 10000) > Y:
        continue
    for j in range(N+1-i):
        k = N - i - j
        if ((i * 10000) + (j * 5000)) > Y:
            continue
        if (i*10000) + (j*5000) + (k*1000) == Y:
            ans = str(i) + " " + str(j) + " " + str(k)
            break
    else:
        continue
    break

print(ans)
