S = input()
T = input()

ans = 'No'

for i in range(len(S)):
    if S == T:
        ans = 'Yes'
        break
    T = T[-1] + T[0:-1]
print(ans)


'''
https://atcoder.jp/contests/abc103/tasks/abc103_b


kyoto
tokyo
Yes


abc
arc
No

aaaaaaaaaaaaaaab
aaaaaaaaaaaaaaab
Yes
'''