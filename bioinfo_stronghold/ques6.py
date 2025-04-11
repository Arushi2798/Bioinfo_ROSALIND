"""
Given two strings s and t of equal length, the Hamming distance between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ in s
and t.
Given: Two DNA strings sand t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)"""

s="GAGCCTACTAACGGGAT"
t="CATCGTAATGACGGCCT"
dh=0
if len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            dh+=1
print(dh)

## another attempt
# def hamming(s,t):
#     return (len(list(filter(lambda pair: pair[0]!=pair[1],zip(s,t)))))