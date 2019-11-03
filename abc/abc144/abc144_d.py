import sys
import math

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, ns().split()))
ns = lambda: stdin.readline()

a, b, x = na()

ans = 0

#area = a * a
#wV = (area) * b
#lastY = b - (x / (area))
#gamma = 2*x / (b*a)
#print(gamma)

#ans = 90.0 - math.degrees(math.atan((2*x))/(a*b*b))
V45 = (a*a*b)/2.0
if x >= V45:
    ans = math.degrees(math.atan( 2 * (a * a * b - x) / (a * a * a)))
#    ans = math.degrees(math.asin(a/2.0/b))
else:
    ans = math.degrees(math.acos((2*x)/math.sqrt( (4*x*x) + (a*a*b*b*b*b))))
#print(area, wV, lastY)
print(ans)


'''
1<= a <= 100
1<= b <= 100
a < x < a**2  * (b)

2 2 4
45.0000000000

12 21 10
89.7834636934

3 1 8
4.2363947991

'''