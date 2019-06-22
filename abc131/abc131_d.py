N = int(input())
AB = [0] * N
B = [0] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))

sortAB = sorted(AB, key = lambda x: (x[1], x[0]))

isYes=True
s=0
for a in sortAB:
    s += a[0]
    if s > a[1]:
        isYes=False
        break

if isYes:
    print('Yes')
else:
    print('No')





'''
5
2 4
1 9
1 8
4 9
3 12

Yes





'''


'''
input
N K
a1 a2 ... an

sample
4 10
6 1 2 7

2


3 5
3 3 3

3


10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352

36
'''