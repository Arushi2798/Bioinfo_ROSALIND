"""The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below."""

file =open("file2.txt","r")
content=file.readlines()
for each in content:
    content1=(" ".join(content)).split(">")

# print(content1[0])
content1.pop(0)
# print(content1)
# print(len(content1))

d={}

for i in range(len(content1)):
    gc,total_len=0,0
    text=content1[i].split("\n ")
    # text.pop()
    # print(text)
    for j in range(1,len(text)):
        # print(text[j])
        for each in text[j]:
            if each=="G" or each=="C":
                gc+=1
                total_len+=1
            elif each=="A" or each== "T":
                total_len+=1

    gcp=(gc/total_len)*100
    d[text[0]]=gcp
    

# print(d)
max_val=0
# res=max(d.values())
for key,val in d.items():
    if val > max_val:
        max_val= val
        max_id = key

print(f'{max_id} \n  {max_val}')