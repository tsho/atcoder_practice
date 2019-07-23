L, R = map(int, input().split())

ans = 2018
R = min(R, L+2020)
for i in range(L, R+1):
    f = False
    print(i, L, R)
    for j in range(i+1, R+1):
        print(i, j, L, R)
        m = (i*j)%2019
        if  m  == 0:
            ans = m
            f = True
            break     
        ans = min(ans, m)
    if f:
        break
print(ans)

'''        
2020 2040

2

4 5
20
'''