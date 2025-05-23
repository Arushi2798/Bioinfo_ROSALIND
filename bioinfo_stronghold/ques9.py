"""Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s
 (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
 of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s
; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s
 if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s."""

# file =open("filex.txt","r")
# content=file.readlines()
# s=content[0]
# t=content[1]

# print(content)
s="AAAGTCTTTTGGGAGTCTTTTGGGTCTTTTCTGTCTTTTCCGTCTTTTGTCTTTTTGGGGTCTTTTGCTGTCTTTTAGGCCTGTCTTTTGCAGTCTTTTAACAGAACGTCTTTTACGGGTCTTTTTAGAAGGTCTTTTAGGTGTCTTTTGTCTTTTGTCTTTTTCGGTCTTTTATACCTGTCTTTTTGGTCTTTTATGAGTCTTTTCTTCCCGATGTCTTTTTGTCTTTTTGATCTTGTTTGTCTTTTCGTCTTTTTATGGTTCTGTCCTATGTCTTTTTGTCTTTTGTCTTTTACAAGTCTTTTGACATGAGGTGGCCAGCGTCTTTTACGTCTTTTGTCTTTTTACGTGTCTTTTAGGGCAGTCTTTTTGTCTTTTCATTCACAGTCTTTTAGGGTCTTTTGTCTTTTAGTAGTCTTTTAGTCTCAGCTCAGTCTTTTTATCAGGAGGTCTTTTGTGCGTCTTTTAGACGTTAGTCTTTTGTCTTTTCGTCTTTTAGTCTTTTGGTAGTCTTTTTGTCTTTTGTCTTTTTCGTCTTTTAGGTCTTTTGTCTTTTACTACGTCTTTTGGCGTCTTTTCCCGTCTTTTCGGTCTTTTGTCTTTTGTCTTTTAGTCTTTTCCTGAGGTCTTTTTATGTCTTTTGTCTTTTGGTCTTTTTGTGCTGATGACCGCCAAATGTCTTTTTGTCTTTTGGAGTCTTTTGCTCAGTCTTTTCGTCTTTTGTCTTTTTGTCTTTTCTGACGTCTTTTAAGGTGGTCTTTTTAGATTAGTCTTTTAACGTCTTTTGCGGGTCTTTTGGTCTTTTTTATGGTCTTTTTGGTCTTTTCCGTCTTTTGCGACGTCTTTTTGTCTTTTCGTCTTTTGTCTTTTAGCCCGTCTTTTCGCTGGTCTTTTGTCTTTTCCTGTCTTTTGGTCTTTTTGTCTTTTCGTCAGTCTTTTTAGATGTCTTTTTCCATCGTCTTTTGTCTTTTGTCTTTTACGTCTTTT"
t="GTCTTTTGT"
# s="GATATATGCATATACTT"
# t="ATAT"
index=[]
# print(s[226:(len(t)+226)])

if len(t)>len(s):
    print("wrong input")
    exit
else:
    for i in range(len(s)-(len(t)+1)):
        if t[0]==s[i]:
            # print("S")
            codon=''
            for j in range(len(t)):
                codon+=s[i+j]
                # print(codon)
            if codon == t:
                index.append(i+1)

print(index)