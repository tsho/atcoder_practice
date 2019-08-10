N = int(input())
s = [''.join(sorted(input())) for i in range(N)]

ans = 0
d = {}
for i in s:
    if i in d:
        ans += d[i]
        d[i] += 1
    else:
        d[i] = 1
print(ans)


'''
for i in range(N):
    s[i] = ''.join(sorted(input()))
    if i != 0:
        for j in range(i):
#            print(i, j)
            if s[i] == s[j]:
                ans += 1
print(s)
res = [s.count(e)-1 for e in set(s) if s.count(e) > 1]
print(ans)
print(res, sum(res))
#for i in range(N):
#    for j in range(i+1, N):



2 < N < 10**5
si < len(si) = 10


3
acornistnt
peanutbomb
constraint
1

2
oneplustwo
ninemodsix
0

5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa
4

2 1
3 3
4 6
5 10

'''