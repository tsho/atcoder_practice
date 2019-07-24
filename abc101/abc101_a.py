S = input()
print(S)
sum=0
for i in S:
    if i == '+':
        sum+=1
    elif i == '-':
        sum+=-1
print(sum)


'''
+-++
2



'''