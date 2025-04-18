"""Ques: In “Counting Point Mutations”, we calculated the minimum number of symbol mismatches between two strings of equal length to model the problem of finding the minimum number of point mutations occurring on the evolutionary path between two homologous strands of DNA. If we instead have several homologous strands that we wish to analyze simultaneously, then the natural problem is to find an average-case strand to represent the most likely common ancestor of the given strands.
Say that we have a collection of DNA strings, all having the same length n
. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.


Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)"""

file =open("file4.txt","r")
content=file.readlines()
s=''
strings=[]

for each in content:
    if each[0]==">":
        s+="\n"
    else:
        each=each.strip('\n')
        s+=each

strings=s.split("\n")
strings.pop(0)
# print(len(strings))

# strings=['ATCCAGCT','GGGCAACT','ATGGATCT','AAGCAACC','TTGGAACT','ATGCCATT','ATGGCACT']

def creatematrix(col):
    m=[[],[],[],[]]
    for i in range(4):
        for j in range(col):
            m[i].append(0)
    return m

def profilematrix(matrix,strings):
    for i in range(len(strings)):
        for j in range(len(strings[0])):
            if strings[i][j]=="A":
                matrix[0][j]+=1
            if strings[i][j]=="C":
                matrix[1][j]+=1
            if strings[i][j]=="G":
                matrix[2][j]+=1
            if strings[i][j]=="T":
                matrix[3][j]+=1    
    return matrix

matrix=creatematrix(len(strings[0]))

profile=profilematrix(matrix,strings)

str_ind={0:"A",1:"C",2:"G",3:"T"}

consensus=''

for i in range(len(profile[0])):
    max_val=0
    for j in range(len(profile)):
        if max_val < profile[j][i]:
            max_val = profile[j][i]
            indx = j

    consensus += str_ind.get(indx)
    # print(indx)

print(consensus)
newdict={}
new_key=["A","C","G","T"]
# key_list=str_ind.keys()
# newdict=dict.fromkeys(key_list)
for i in range(len(new_key)):
    newdict[new_key[i]]=profile[i]
# print(newdict)


for each in newdict:
    print("\n",each,end=": ")
    for i in newdict[each]:
        print(i, end=" ")


## another attempt

# import numpy as np
# profile= np.zeros()
