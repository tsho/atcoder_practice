N = int(input())
p = list(map(int, input().split()))

ans = 'NO'
p_sorted = sorted(p)

print(p, p_sorted)
cnt = 0
for i in range(N):
    if p_sorted[i] != p[i]:
        cnt += 1

if cnt < 3:
    ans = 'YES'
print(ans)


'''
5
5 2 3 4 1
YES

5
2 4 3 5 1
NO

7
1 2 3 4 5 6 7
YES
'''
