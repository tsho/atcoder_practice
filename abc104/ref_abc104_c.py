# 参考https://atcoder.jp/contests/abc104/submissions/2953603
import sys

stdin = sys.stdin

# lambda式で以降で使えるようにする
ni = lambda: int(ns())
na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

# 標準入力を変数とリストに格納
D, G = na()
p = []
c = []
for i in range(D):
    x, y = na()
    p.append(x)
    c.append(y)

ans = 99999999
# bit全探索
# 1bitをD（レコード数）シフト
for i in range(1<<D): 
    ct = 0
    score = 0
    # 完投の場合の全パターン
    for j in range(D):
        # iを右へj bitシフト。
        if i>>j&1:
            score += c[j] #全回答の場合のボーナス得点
            score += p[j] * (j+1) * 100 #（完投の場合のボーナス得点以外の全得点数）
            ct += p[j] #完投の問題数
    # D-1, -1, -1 -> 2の場合、1, -1, -1 -> 1, 0
    for j in range(D-1, -1, -1):
        # ビットシフトして1ならとばす
        if i>>j&1: continue
        # scoreが基準以上かどうか
        if score >= G: break
        # 多い方から計算
        g = (j+1)*100
        # got は Gは超える点数 - score(完答) + g - 1 
        got = (G - score + g - 1)//g
        score += min(got, p[j]) * g
        ct += min(got, p[j])
    ans = min(ans, ct)
print(ans)
