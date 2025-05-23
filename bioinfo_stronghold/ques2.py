"""Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t
 with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t."""

# t="TCCCCCCCCTCAGACCGCGACCGGACGATATTCTTGTTATAAATGTGTCGAGGCCATCCGACTATAGTACGATCTCACAATGACCCCTATCCAGCCCGTTTTAGTTCTCACCAGTGGAAATACTATTTTAGCTTGATTGGACGGACTTGTGAAGGCTACCAATATTTCGTTCGTCGTTTCCTTGGCGTATGCTACCGGGTAAACTCTAGAGGCACAGTGAGGACATACGGACCGAGGTACCGCAATTATAACGTGCATGTTTTGGTTGTTGCGTTACCTGCTGTGCATCCCTATACCGGCAATGTGAGAACCTGTTATCGGCTCGCACGACGTAAGTAGTCCCGAGGAACGCCGTACCACACCTATGTTCGATGGCTCCGTAGATGGCCAAGATAATGCCGAACACACGTGCATCGGCCCTAATAGGTGCACCAGTGATCATTTGAAATAACCAGCCGCCATGGTTGACACCGCAAGCTTGGTCATACAACATGAATCTTGTTCGATACCCTAGTGGATAGCTTTGGAACCCCGGCGCGGGTATGTGATTTTACACCAAGGATTTGCTGAAAGGACACTTCCAGACGATTTATGTGGGACAGGTTCTCAGAGCGGATCATGGACTATGGACGTAAAGTGCCCTGTTAAACTTTAGCATGGCTCAAACCCAGTGCTCGTATCTAGTCGGCCTCTAACTAAGACGGAGGTTTTATATGGCGCAAGAGGCGATCCGAATCGCGCTTTTGCCCAACTGAAAAACCTCCTCAAATAGCGTGCCGACAAGGTTGTGTCTCGCATTTTACACTTATACGTCCTAGAGTCATTGGTTATCACGCCGCGGGTAAAACTGAAGGGATTATCGGCTTAGCGATTGACCCTGTTATATAGGGATGGGGGCCAGAGCTGTCCCTTTCCCAGTTGTGATCTCACATCCGCACGTAACGTGAGGGTACCTGTC"
# # t="GATGGAACTTGACTACGTAAATT"
# u=''

# for each in t:
#     match each:
#         case "A":
#             u+="A"
#         case "T":
#             u+="U"
#         case "C":
#             u+="C" 
#         case "G":
#             u+="G"

# print(u)

##another attempt
dna = "GATGGAACTTGACTACGTAAATT"
rna = dna.replace("T", "U")
print(rna)
