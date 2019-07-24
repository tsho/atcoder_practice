A, B = map(int, input().split())

if (A * B * 1) % 2 != 0 or (A * B * 2) % 2 != 0 or (A * B * 3) % 2 != 0:
    print('Yes')
else:
    print('No')

'''
https://atcoder.jp/contests/abc109/tasks/abc109_a
3 1
Yes

1 2
No

2 2
No
'''