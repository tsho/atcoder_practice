n, x = map(int, input().split())
l = [int(i) for i in input().split()] 

d = 0
i = 0
if x > 0:
    while d <= x:
        d = d + l[i]
        i = i + 1
        if i >= n:
            break
    if d > x:
        print(i)
    elif d <= x:
        print(n+1)
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