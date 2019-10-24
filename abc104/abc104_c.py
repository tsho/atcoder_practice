D, G = map(int, input().split())
p = [0]*D
c = [0]*D
for i in range(D):
    p[i], c[i] = map(int, input().split())

print(p, c)
cnt = 0
score = 0
for i in range(D-1, 0, -1):
    for j in range(p[i]):
        cnt += 1
        score += (i+1)*100
        if score >= G:
            break
    else:
        score += c[i]
        if score >= G:
            break
        continue
    break
print(cnt)

'''
2 700
3 500
5 800
3

2 2000
3 500
5 800
7

2 400
3 500
5 800
2

5 25000
20 1000
40 1000
50 1000
30 1000
1 1000
66


'''



