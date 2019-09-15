S = str(input())

ans = 'Yes'
for i, step in enumerate(S):
    odd_even = (i+1) % 2
    if odd_even == 0:
        if step != 'L' and step != 'U' and step != 'D':
            ans = 'No'
            break
    elif odd_even == 1:
        if step != 'R' and step != 'U' and step != 'D':
            ans = 'No'
            break
print(ans)

'''
5
5 2 3 4 1
YES

5
2 4 3 5 1
NO

7
1 2 3 4 5 6 7
YES
'''
