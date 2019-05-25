abc = input()

if abc == 'A':
    print("T")
elif  abc == 'T':
    print("A")
elif abc == 'C':
    print("G")
elif  abc == 'G':
    print("C")



'''
https://atcoder.jp/contests/abc122/submissions/5329221
p = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}
 
print(p[input()])


https://atcoder.jp/contests/abc122/submissions/5333029
pat = str.maketrans("ATCG", "TAGC")
print(input().translate(pat))


https://atcoder.jp/contests/abc122/submissions/4687604
print("ATCG"["TAGC".find(input())])
'''
