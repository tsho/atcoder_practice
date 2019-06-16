tm = []
a = int(input())
tm.append(a)
b = int(input())
tm.append(b)
c = int(input())
tm.append(c)
d = int(input())
tm.append(d)
e = int(input())
tm.append(e)

total = 0
#print(tm)
m = tm.index(min(tm, key=lambda x: int(str(x)[-1]) if (str(x)[-1] != "0") else 10))

tmp = tm.pop(m)

print(tm)

for x in range(len(tm)):
    total = round(tm[x], -1) + total
    print(total)
total = tmp + total

print(total)
