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

if L*R < 2019:
    print(L*R)
elif (L*R) == 2019:
    print(0)
elif R < 2019:
    print(L)
else:
    aa = L//2019
    if (L%2019) == 0 or (R%2019) == 0:
        print(0)
    elif  L<((aa+1)*2019) and ((aa+1)*2019) <= R:
        print(0)
    for i in range(1, 2018):
        if  L<((aa)*(2019+i)) and ((aa)*(2019+i)) <= R:
            print(i)
            break



2020 2040

2

4 5
20


#a = map(lambda x: (1/x)%2019 if ((1/x)%2019).is_integer() else 1000000000, n)
print(n)
print(a)
print(min(a))

d = 2019
#逆元
#for i in range(L, R):
n = list(range(L, R+1))
#for i in range(L, R):
#    for j in range(i+1, R):


'''