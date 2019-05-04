crd = []
a = int(input())
crd.append(a)
b = int(input())
crd.append(b)
c = int(input())
crd.append(c)
d = int(input())
crd.append(d)
e = int(input())
crd.append(e)
k = int(input())

#print(len(crd))
for x in range(len(crd)):
    for y in range(x+1, len(crd)-x):
        #print(x, y)
        #print(crd[int(x)], crd[int(y)])
        z = k - (crd[y] - crd[x])
        #print("z= ", z)
        if z < 0:
            print(":(")
            break
    else:
        continue
    break
else:
    print("Yay!")



