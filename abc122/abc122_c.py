#in writing
import re

def calmax(i):
    return max(map(len,re.split('[^ACGT]', i)))

n, q = map(int, input().split())
#print(n, q)
s = input()
#print(s)
lr = [ print(s[int(input().split()[0]):int(input().split()[1])]) for i in range(q)]



#lr = [print(calmax(s[int(input().split()[0]):int(input().split()[1])])) for i in range(q)]



'''
8 3
ACACTACG
3 7
2 3
1 8
'''