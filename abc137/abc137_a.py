A, B = map(int, input().split())

plus = A + B
minus = A - B
multiple = A * B

ma = max(plus, minus)
ma = max(ma, multiple)

print(ma)

'''

'''