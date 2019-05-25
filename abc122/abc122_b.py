s = input()
acgt='ACGT'

x = 0; l=[]
for c in s:
    if c in acgt:
        x += 1
    else:
        l.append(x)
        x = 0
l.append(x)
print(max(l))

'''
https://atcoder.jp/contests/abc122/submissions/4703467
import re;print(max(map(len,re.split('[^ACGT]',input()))))



https://atcoder.jp/contests/abc122/submissions/4703846
p=m=0
for c in input():p=-~p*(c in'ATGC');m=max(m,p)
print(m)

'''