r, D, x = map(int, input().split())

for i in range(10):
    temp = r * x - D
    print(temp)
    x = temp

'''
r D x2000

2 10 20
30
50
90
170
330
650
1290
2570
5130
10250

'''