w, h, x, y = map(int, input().split())

s = w * h / 2.0
if w == (x * 2.0) and h == (y * 2.0):
    c = 1
else:
    c = 0
print(s, c)

'''
W　H x y
面積　分け方複数1, 一つだけ0
2 3 1 2
3.000000 0


2 2 1 1
2.000000 1

'''