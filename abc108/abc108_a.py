K = int(input())

if K % 2 == 0:
    odd = K // 2
else:
    odd = (K // 2)+1

even = K // 2

print(odd * even)

'''
https://atcoder.jp/contests/abc108/tasks/abc108_a
3
2

6
9

11
30

50
625
'''