s = input()

tmp='a'
flg=0
for a in s:
    if tmp == a:
        flg =1    
    tmp = a

if flg ==1:
    print("Bad")
else:
    print("Good")

'''
3776
Bad

8080
Good

1333
Bad

'''