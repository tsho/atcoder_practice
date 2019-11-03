import sys

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline()

N = ni()

ans = "No"
for i in range(1, 10):
    for j in range(1, 10):       
        if (i * j ) == N:
            ans="Yes"
            break
    else:
        continue
    break

print(ans)


