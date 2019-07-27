N = int(input())

S = sum(list(map(int, list(str(N)))))

if N % S == 0:
    print('Yes')
else:
    print('No')


'''
https://atcoder.jp/contests/abc101/tasks/abc101_b
12
Yes

101
No

999999999
Yes

'''