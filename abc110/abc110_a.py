ABC = list(map(int, input().split()))
mi = ABC.pop(ABC.index(min(ABC)))
ma = ABC.pop(ABC.index(max(ABC)))
print((ma * 10) + ABC[0] + mi)


'''
https://atcoder.jp/contests/abc110/tasks/abc110_a
1 5 2
53

9 9 9
108

6 6 7
82
'''