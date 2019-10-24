n = input()
A = list(map(int, input().split()))

cnt = 0
for a in A:
    while a % 2 == 0:
        a //= 2
        cnt += 1
print(cnt)

"""
3
5 2 4

"""