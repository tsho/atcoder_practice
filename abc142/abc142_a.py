N = int(input())
mod = N % 2

if N == 1:
    print(1.0000000)
elif mod == 0:
    print(0.500000)
elif mod == 1:
    print((float((N//2)+1)/float(N)))
'''
'''
