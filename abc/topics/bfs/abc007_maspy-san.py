# ref:https://atcoder.jp/contests/abc007/submissions/7803134

import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

R,C = map(int,readline().split())
sx,sy = map(int,readline().split())
gx,gy = map(int,readline().split())
grid = ''.join(line.rstrip().decode('utf-8') for line in readlines())

start = (sx-1) * C + (sy-1) # １次元問題に変える
goal = (gx-1) * C + (gy-1)  # １次元問題に変える

INF = float('inf') 
dist = [INF] * (R*C)  # INFをRxCの数だけ配列を作成する
q = [start] 
dist[start] = 0
while q:
    qq = []
    for x,dx in itertools.product(q,[1,-1,C,-C]): # デカルト積になるので qx1, qx-1, qxC, qx-Cのパターンでループ
        y = x+dx
        if dist[y] != INF or grid[y] == '#': #INFでないか壁にぶつかると飛ばす
            continue
        dist[y] = dist[x] + 1 
        qq.append(y)
    q = qq

answer = dist[goal]
print(answer)


