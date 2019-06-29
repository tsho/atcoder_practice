import numpy as np

n = int(input())
d = list(map(int, input().split()))
d = np.array(d)
d_sorted = np.sort(d)

half = int(n/2)
if d_sorted[half] == d_sorted[half-1]:
    cnt = 0
else:
    cnt = (d_sorted[half]) - (d_sorted[half-1])
print(half, d_sorted)

print(cnt)

'''
6
9 1 4 4 6 7
2

8
9 1 14 5 5 4 4 14
0

14
99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1

'''


