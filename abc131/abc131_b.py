N, L = map(int, input().split())

score=[]
for i in range(N):
    score.append(L+i+1-1)
print(score, min(score))
score.remove(min(score, key=lambda x: abs(x)))
print(sum(score))
#print()


'''
input
N L
N:apple number
-100<L100

味
L+i−1
 
ex1
5 2
18

3 -1
0


ex3
30 -50
-1044

'''