n, x = map(int, input().split())
l = [int(i) for i in input().split()] 

d = 0
if x > 0:
    for i in range(n):
        if d > x:
            break
        d = d + l[i]
        print(x, l[i], i, d)
    if x >= d and i == n-1:
        print(n+1, n)
    else:
        print(i)
elif x <= 0:
    print(1)
'''


n x
l1 l2 ... ln-1 ln

3 6
3 4 5
2

4 9
3 3 3 3
4

'''