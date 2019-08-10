S = input()

ans = [1] * len(S)
tra = [0] * len(S)
print(ans)

continas = False
ans = []
tmp = 0
lst_cut = 0
for i in range(1, len(S)):
    if S[i-1] == 'L' and S[i] == 'R':
        ans_tmp = [0] * len(S[lst_cut:i])
        cnt_R = S[lst_cut:i].count('R')
        cnt_L = S[lst_cut:i].count('L')
        if cnt_R == cnt_L or  (abs(cnt_R - cnt_L) % 2 == 0):
            ans_tmp[tmp:tmp+1] = cnt_R
        elif cnt_R > cnt_L:
            ans_tmp[tmp] = cnt_L
            ans_tmp[tmp+1] = cnt_R
        elif cnt_R < cnt_L:
            ans_tmp[tmp] = cnt_R
            ans_tmp[tmp+1] = cnt_L    
        ans = ans_tmp
        lst_cut = i
    elif S[i-1] == 'R' and S[i] == 'L':
        tmp = i - len(ans)

#for i in range(1, len(S)):
print(' '.join(str(x) for x in ans_tmp))

'''
S[0] = R
S[N-1] = L
S[:] = 1

10**100
連続しているところはまとめる


RRLRL
0 1 2 1 1
00010
 RRL RL

RRLLLLRLRRLL
0 3 3 0 0 0 1 1 0 2 2 0

 RRLLLL RL RRLL

RRRLLRLLRRRLLLLL
0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0

 RRRLL RLL RRRLLLLL

RL 0
11

RRL 1
012

RLL 1
210

RRLL 0 
0220

RLLL 2
2200

RRRL 2
0022

RRRLL 1
00320


RRRRLLL 1
00320






9

0 3
IMPOSSIBLE

998244353 99824435
549034394

N = int(input())
H = list(map(int, input().split()))

ans='Yes'
flag=True
if N > 1:
    tmp = H[0]
    ma = H[0]
    for i in range(1, len(H)):
#        print(i, H[i], tmp)
        if (H[i] - tmp) >= 0:
            tmp = H[i]
#            print('=   0')
            mi = max(H[i-1], ma)
            flat=True
            continue
        elif (tmp-1) >= ma and ((H[i] - (tmp-1)) ) >= 0 and flag:
            tmp = H[i]
#            print('-1')
            mi = max(H[i-1] - 1, ma)
            flag = False
            continue
        else:
            ans = 'No'
            break

print(ans)



1<N<10**5
1<H<10**9
5
1 2 1 1 3
YEs

4
1 3 2 1
No

5
1 2 3 4 5
Yes

1
1000000000
Yes


3
1 20000 19
No

3
1 2 3
Yes

3
9000 9
No

3
1000000000 1000000000 1000000000
Yes

3
2 2 1
'''