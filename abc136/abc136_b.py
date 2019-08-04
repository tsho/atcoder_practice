N = int(input())

ans = 1
if N < 10:
    ans = N
elif 10 <= N and N < 100:
    ans = 9
elif 100 <= N and N < 1000:
    ans = 9 + (N - 99)
elif 1000 <= N and N < 10000:
    ans = 909
elif 10000 <= N and N < 100000:
    ans = 909 + (N-9999)
elif 100000 <= N and N < 1000000:
    ans = 90909
elif 1000000 <= N:
    ans = 90909 + (N-999999)

print(ans)

'''
M < 10**5

9
9

'''

