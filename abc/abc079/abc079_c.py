# 参考:https://atcoder.jp/contests/abc079/submissions/1782809
import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

ABCD = [int(_) for _ in ns().strip()]

for i in range(8):
    t = ABCD[0]
    
    for j in range(3):
        if i>>j&1:
            t += ABCD[j+1]
        else:
            t -= ABCD[j+1]
  
    if t == 7:
        print("{}{}{}{}{}{}{}=7".format(
            ABCD[0], "+" if i>>0&1 else "-",
            ABCD[1], "+" if i >> 1 & 1 else "-",
            ABCD[2], "+" if i >> 2 & 1 else "-",
            ABCD[3],         
        ))
        break
        
