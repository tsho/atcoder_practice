import sys
import math

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline()

s = ns()

print(s)

aa = []
pre = ''
cnt = 0

aa.append(0)
for ss in s:
    if ss == '<':
        cnt += 1
    elif ss == '>':
        cnt -= 1
    aa.append(cnt)
print(aa)
print(sum(aa))
if min(aa) < 0:
    m = min(aa)
    aa = map(lambda x: x - m, aa)

print(sum(aa))





'''
<>>
3

<>>><<><<<<<>>><
28
'''