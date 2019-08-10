N = int(input())
H = list(map(int, input().split()))

ans='Yes'
pre=-000
if N > 1:
    for i in range(0, len(H)):
        if (pre <= H[i] - 1):
            pre = H[i] - 1
            continue
        elif (pre <= H[i]):
            pre = H[i]
            continue
        else:
            ans = 'No'
            break

print(ans)


'''
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

'''