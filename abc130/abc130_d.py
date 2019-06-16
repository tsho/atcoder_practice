n, k = map(int, input().split())
a = [int(i) for i in input().split()] 


cnt=0
for i in range(1 << n):
    output = []
    o = []
    flg = 1
    for j in range(len(a)):
        if ((i >> j) & 1) == 1:
            if flg == 1:
                if o:
                    output.append(o)
                o = []
                flg = 0
                o.append(a[j])
                print(o, a[j])
            elif flg == 0:
                o.append(a[j])
        else:
            flg = 1
#    print(o, a[j], 'outside')
    if o:
        output.append(o)

    print(output)
    c = 0
    for l in output:
        print('sum l ', sum(l))
        if sum(l) >= k:
            c=1
#            print('over k ', output, sum(l))
    
    cnt = cnt +c

print(cnt)

'''
input
N K
a1 a2 ... an

sample
4 10
6 1 2 7

2


3 5
3 3 3

3


10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352

36
'''