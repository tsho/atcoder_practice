S = []
tmp = input()

for i in tmp:
    S.append(i)

isYes='Yes'
for i in S:
    if S.count(i) != 2:
        isYes = 'No'
print(isYes)

'''
ASSA

'''