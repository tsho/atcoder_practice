N = int(input())
AB = [0] * N
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