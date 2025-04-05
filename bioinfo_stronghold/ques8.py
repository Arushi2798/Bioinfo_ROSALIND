"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string [Math Processing Error]
 corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by [Math Processing Error]."""

d={'UUU': 'F','CUU': 'L','AUU' :'I',      'GUU' :'V',
'UUC': 'F', 'CUC': 'L',     'AUC' :'I',      'GUC' :'V',
'UUA' :'L', 'CUA': 'L',     'AUA' :'I' ,     'GUA' :'V',
'UUG': 'L', 'CUG' :'L',      'AUG': 'M' ,     'GUG': 'V',
'UCU' :'S', 'CCU' :'P',      'ACU': 'T'  ,   'GCU' :'A',
'UCC': 'S', 'CCC': 'P',      'ACC': 'T'   ,   'GCC' :'A',
'UCA': 'S', 'CCA': 'P',      'ACA': 'T'    ,  'GCA' :'A',
'UCG': 'S', 'CCG' :'P',      'ACG': 'T',      'GCG': 'A',
'UAU' :'Y', 'CAU': 'H',     'AAU' :'N'  ,    'GAU' :'D',
'UAC' :'Y', 'CAC' :'H',      'AAC': 'N'  ,    'GAC' :'D',
'UAA' :'Stop','CAA' :'Q' ,     'AAA': 'K' ,     'GAA' :'E',
'UAG' :'Stop','CAG': 'Q' ,     'AAG' :'K'  ,    'GAG': 'E',
'UGU': 'C', 'CGU' :'R'  ,    'AGU' :'S',      'GGU' :'G',
'UGC': 'C', 'CGC' :'R'   ,   'AGC': 'S' ,     'GGC' :'G',
'UGA' :'Stop','CGA': 'R'   ,  'AGA': 'R'  ,    'GGA': 'G',
'UGG': 'W', 'CGG': 'R'      ,'AGG' :'R'  ,    'GGG': 'G' }

file =open("file3.txt","r")
content=file.read()
print(content)

# s="""AUGUGCAUCACCCGGAUCGACGCGGCGUUCGUUAGUGCACUAAAUAUAGUGAAUGACCACUCGUGGAGCAAUACCGGUCUUCUGUGCCCUGUAGGAGCACGUUCUGUUAGAGCGUCGCCCCCAUGGGUAAAGAGUCUCUCAGAGACCGUGAUGGAGUUAAGGCCUACUGUGCACACGCUCUCGGUGGGUCCGAAGAACACUGCUAAGGCUAGGACGUGCCAGAUACGAGUGCGCCGGCUAGUUCGCAAACUGACGUCUUUUAAAUCCGUAGACACACGACCGAUAGAUGGCGACGACAUCGGCGAGUGUUAUUACCGUUUAGAGCCGAUUCAAAGCCCAUCCCAACAAGCUAACAUGUCCGGGGCAAACCGGGCCAGCGCUCCUAACUGUGAUGACGUUGAGUGCGACGUUUCGAUGUCAGUGUUUCGACGCUACCCUAUCCUGAUCAUACCGUUAAGCUGCGGUGUACGCGAACCCCGGAGGCCCACGGUAGGAGCCACUAGUGAGCAGCUUUUGAUAAAUACGGUCUUUCCUACCUACCGCUCCUCUGCCCACGCGCUUGGAGUAGACGUAUCCGUAGAACACGGUUGCAUUAUGUGUGCAUUGGACCGAGUAGUUAGCGAGUUAUGGAGCAAUAUCAUGGGCACUAGGACAGAAAUAAUCAAAUCCAGGCUCCGACAUAGUAAUACACCAUUCACCGAUAGUUCCGCCCGGUCCCCAGCCGAACUCUUCCCAUCGGUUGCGAAAAAGCGUUGGCCCCCCAGAUUUCUUUCUGUUCAGUUUGACUGGAACCCCCGCUAUAUGGCAUCUACCAAUCAUCCACAACAGCACCGAGUGCCAUUGGGUAGGGCACCAGCAACUCGCAAGGAUUCGGCUUGGUUCCCACCACUAGUCACAGUCUACCCAUGCAUGAUCACGAGUAUAUUUCGUCCGCUGAGAGAGGUGCAGAAGUCGCCGGGAGGCCGCCGAAAUAGGAGUGUCUUCAGACGCAGCUACAGCCGAAUGUCAGGGAGAAACAGAUCCUCGUCUUUCUAUCACCUACACGAGAGCAAAGUAUCUAAGCAUUGGAUAAGCAGCUCCGGUUCUGGCCGUCGAACGUGUAAAUGGCAUCGCCGAUCCAGGGAGAUUAUCGAUUGUUCGCGGAGCGCCGAUCCGCAUCUGACACAUGGACUAGGGCCACACCCGGGCACCGAGAAGAGAUCGCUUACGAGCCAGCCGUUACCCCAAUCAGUCGGGUUUACCAUCAACGAUCGCACACCGGAGGGCACCUUAAAUCGUUGUAGAGGGCGCUUAUUGACGGCACCCACGCAGAAUGUCAGUAAACUCAGUUGGCUUGAUAGAACCACACCUGAAGAAUCGAACUUCAUUGGCCUAUAUAACCUAAGGAAGAUAGAAUGCGGGGGAGAACUUGCUUGCCGUGUAGGCUUUUUACAGAGAAGCGCUGCGGGACAUACGGGAACGCCUAAUUCAAGGUUUGUCUUUGCCGGGCCUAAGCGGGGCCGAGUAGGGAUUCGCCCAUCUCGUUUCAUGGAUUGGUCCAGCCCUUCGAUCCACCGCAUAUUGCUGAAGCGGGGAAAGCAAGAAGGUAUAGGGUGGCCUCCUCGAUCCCUGUCGCGCCCGAAUGCAUUCAAAGUAUUACGUACCAAAAUUAACUGCGGACCUGGAGAUACAUAUCGUCGACGUCUAAAUGGUCGAUUGGCCUUACAGGAAGGCCUACGCACCAUUAUUUACCCACGUUUAACAGUGGGUGAUCAACCGACACAUGUUCAUGUAGAGCCGCUUUCAACACGCUCAGUUCGUGAGGGCGCACAUGGAGUGUUAUUACAAUACCAGGCGGGAACAUUCGUUAGCCUAGCCUGCAUCCAAGGUGAAUCGUCAACCUUAUGCGCUGAUCGUCAUAGUAGCUCUAACCGACACAAGUGGGCUGAACGCACUAAUCCCCCGUGCAGAGCGAUGACGCGGCCGCCCAACCCCCCUGUGAUCUGUUGUCCGUGGUGUGCCAGUUCCGGAGAUCGGCGGUCCAGUAGAGGUAACCUAAUUCACAUGGUUAUUUUGUGGCAAUUAUCUAGAAAUAUCAGACACGCCGCCUCAAAUGAAAUUUUGGUCAAUAGGCAAGUUACUAGAGCUCCGUGCUCGACUGACUGUAGUGGCGACGUAUGCCACACGUUAGGUAGAUUUGCACAGCGGAGCCAAUCACGGUGUCAGCCGGUCGCCAACUACGCAGAAGUGAAUUGUCCCGCAAAACAUUUUGAACUGGGGCGCUUGCGUGUGUGGAGUGUAAUCCGAUCGCGAGUGACACACGGUUGGUAUGGCAGAGAGGUUUGCUUUAAAUCGGGCUCCAUACUCAACGCCAGGUUUGACCAUCUUCAAUCGGCACGAGUUGCAAGGGACGUUUGGAGUAUUCCAUGCAGGGUGUCUAUUCGCGAACAUAUAUGGCCGAAGGCCUCGAUGAGCUCUUAUUGGUCGGGACUUCUAUGGGGGUGUUGGACCCUUAUAUCCAGCUCAGCCUUGGCACGCGGUGAUGACUGCUAUGCUCUUUUAUCCAUAACUCCACAUAUUGUAAGCUAUUACGGGCUUACACUCAAUUUCAUACUCAUUAAGAUUUCAGAUAUUGUCGCCGCAGCUUUUCGGGGAUCCGCCUGUCGUUUGAGUGAUCGGAAAUAUAUAAAGAGUAAUGAGCGCUCCAAGUACACCGGUACAGACGUAUGCAAACUCCGGGGUGCACUGUGUCCUCCCAAACGUGUUUACUUUUGGAUGACCAAAUCAAUUCGUGACUACGAGGAAUACAACUCAUUGGACGUUGCCGUCUCGGGGAGGGUGGUCAAGAGAGUGCAGCAAAUAUGGGUAGUUUCGUUGGCUUAUCGCAACAUGAGUUAUUCACCCGGAGUUGACUGCUCUCCGCGUGGGUGCUCCCAAUAUGUGACGUUAGCGUUACCUAACUCUGCAAAAAAUACCCCCUCCUGCAGCCUUCAAUUUCAUCCAACAUCGAACUCAAAUACUCGGUACCUUACUCAAAAGCUUGACGGGACCUUACAGGCCCCCAAAGCUGGGGGGCUUUGUUUAUUAGUCUCGCUCAUAAACGAUCGCGCCCCGGGUAACAGGAUGGAACAUAAGGCGUCGGUACAAGCCAGUAACUCCGUACACAGUGGAAGGCCGGCAUCGUCGGACUCACGGGUUACGAAGAUCACCAAAAAAUAUGAUAACGCGCUUGAUCGUUGGUCUAUUGUCGGCUUGAAAAGAAUUCAGCAACUUUUCGCCCUUGCGAUCAUAGCUUUCUCGGGAAAUGCACUGCGCCACGUUGAUUCAGAUUUUAGUCCAUUCCUUACACCGUCCUUCGUGGCGACAAGUUUGGUUGGUACCGGAACCUGGAGGUCUGCCCCAGGGGCUAAACGGCAGAAAAACCAAACUAGCCGACCAUUUUCGCUCUCAGACAACGUAAGCCACCCGGGAAUAUCAAAAGUGGAUGGGCACUGGAGAUCCCCUUACAGAGUCUAUGACUGCCGGUUUCCACAACCCAAAGAGGGUUCGAACUGCGUUACAUCUCAAGGCUCGGCAUUUUGCAUUCGGCCUGCGACUGCAACGGAUCCUCGGGUAAAAAAGCUAUUAGCACGCUCGGAGAUUGUCGUGCCGACUUUGGUCUUGAAGGUGGUAACGCAACUAGGUCAGGGUACGGCCUACCCGGGAAAUCCUCUUAGCGGGGAUGAUUAUCCCGGGUUUAGGACAUCUUGCGCACACGAGACAAGUGUCCGUUACGUUGCGUUUGUCCACCAUUGUGUUCGCUCCCCGGAUUCACUUUCUCUUCGACACAACCAGGGUAACCAUAAUGUCGGCUCCGUCUUAGAUGGAUGGACCAAGGAGACUCAACUAGAGAGUUACAGUGGGUGGGCGCGGUACCUAAUUGGUAAAUCUACUAAUCCUCUCGCGAUGGGGCGCGAUUUGCCGGACGGCGUCACGGUUCUAGAAUUAGAGCGGAGACUAUAUGCUUGCCGAAAUGUGUACUCCCAAAUAUACCGCAGUGCUAAGCCUGACAUAUGUUUCUGUAAAUCUCCUGCCUACGACCACGUCGCCGCGUCAGUAAAUCACGUUGCUCCUUUAUUACAACUUUUUCAUUAUAUAUCGGACGAGUUACUCAACGUAUCCGAGGGCCCGACCAACCCCUUCAGACCCCUUGGCGAGAACUCAGUUCGACACACGGCUAACAUCUAUAUCGUUGUGAGAUCCGCUGGCCUAAGCUGCUGGUAUAUGUGCACUGAGCUUGACGAUCAAGGUUGUCGCAGGAAAUGGCCAUAUCAGGAAGUCUGUAGUAAGCGCAGCAUUACGCGUAAGUCGGCGGGUCACCGUUAUCUUUGGAAAUCGCGUAGCGACCUUUCCCUGAAUAAGUGGCUCCGCCCUGUAUGGCCGGAGCUAGUAUUUAUAAUUAAUAUCAAGAGAAAUGAGCUCCGGGUUUCCAUAGGGAAAGCUGGAACGCACAGGUUUGGCAAACCGACUGAUCAAGUCUCGUGGUCGUACGCGCAUCGUUAUUGCAAGGUCAUAAGUAAGUUUUUACUGGUCGAGAAGCAGAGGAAAGCGAAGCGGCGUGCCCUAGAUGCUGGCGUUAACUCUUACUUCGUGCCGAGCCCACCACAUUAUGUUUUGUUACGACAUCUAGCCAAUGCGAAAAGUCUUGAUGCACUGGUGAUCUCAUUGGGGGUCACUAACGAGUCCCUCGACACCAGCAGGAGCCGAACGGCUCUGGCCCGCUUACCGAGCUUCAAGCAAGAUUGGCCUAUUGCAUUAGAAGGCCUUUUGGCGGCGGACACGUUCUCAUUUCACGAUACACGACCACGCCGAGCAAUCACACCGGCCUACACAACGAUUCCGGCUAUCAGGAUCAUUCCGAUCAAUCAGUGCAGAGGUCAAAACAGAUGGACGAUAUUCGUGCGGAUAGGCCAGGUCCCCUCACGGGCAAUGUCUGGGUUAGCAACGGCUCCUACCCAUAUGAUCUACACGUACUAUAAUGACAAUACAAAAUUUUUCAUGGAGGUAUCGGGCAGGCGUGUAAAGCAAUUCGCAUCUAAGAUAUUGACACUUCUCGUUGUGAUGAGUUGGAUCGGGUCCCCGUGGGCGUACGCGAAGAUUUGUCAAGCGUCCAAUAGAAGCUCGACGGCCGUCGAAUGUGCAGAGCCAUUUUCUCGCGAUCAGGGGGCAGUCAGACGACUAUGCAACAAUCUCUACCUACACUUUCCGUUAUGGUUGGGCGUGAUCAAAGGCAUAACGGCGGUAUCACGGGCUCCCAGUAAACUCAACCGAGGCACCUGGUCACAGCGACAUUGGCAUGCUUUAGAGGGUCACGACCUACUUCCAGGGUGCAGAAUAUCGGGCUGCCCAGACUGGCCAUGUAAUACACUGGUGCGUCACCCCUUCAGGCAUUGUCAGCCCGAUCUAGACAAAUUACCACACUAUUGGUUACAUGGUACCGUUGGCCCCCCACUAGGGAUUUUUACGCGGCAUGCCAUUCUCAAACGUGCUAUAAGUAGUUUCCAUCAAACGCGACUCUUCUGUUCUAUACGCUGGAAAGACGCCCAAGUAGUUGAACGGGUCGGCGCGGUAGUCGAUGUUUCCCGUAGUAUAUCACCUAUCAAUAUGAUCGCAGGAGAAAGCUCCCGCAAUGGCGAACCUAACUUGAGGCCUUUGCAAUGUGCGACGGCACAAUCCUCACGUGUAUUUACUGGCCGGAACUCUCAGAUCAUAACGAAGAAGUGCGAAGACCACGGCAGAAACCAUUUACGCAGGUAUCCUGCAAGCCUUUUUUGGCCAUUACCAAAAAGUCUUCUUCGCCGAACUCGGAAAUCCAUUGUUACCUCACCUAGUACAGCAGCCUCCGAGCACAUCAUGCCCGAGAGAUACCAAGGCAGUCACGUGUUAACAAUGCAUCUUUUGUUAGUUGUAGGAACGCUGCCCCACGAUAUCGGCAGUAUCUACUAUGACGAAGAGGGGUGGGAUCCCACCAGCAAUGGUAUCCGAGCUGCAGUUUAUAGGGAUUUCACUAGCGCCGGGGCCGCAUGGCCUGUGUGCUCGGGCGAUCUAGACGCUACAAGGGCAUAUGCUUACACGGAAAAUGUAGGACGGCCGGCGAGUCGUCGUAGACGGCGGACUAGCGUUAAACGCAGCAGACUUUUUGUUUUGCACACUUGGCGCGACCGUCAACCUCGAGGGGCAGAACUUCGAGAUCCUCAUCGGGUGCGACACCAGAGCCGCAGUCGGUUUAAUCCUAAUUCCCACUUGUUAUCUUGGGGAACGAUCGAGUACUUUUGUCUCUUGCGCAGGGCACCCGCCCGUGGCAAGAGAAGGUACAUACCUAACUCUGAUGUGCAGGACCGGAUUUGGGCGAGUUACUCGCACCCGGAGAUGCUCCUAGUCGGUUGCAGGAAGAUGAGAGGUCCCCACGAGUUACUUAUCCCCCGUGCUACUGUCGUCCGCUCAAUCCACAAUGUCGGCAACAGGCCGCCUUCUUUGAAGGCGGAGGGCUUGCAGUCGGGUUCGAAAUGGUGGAGGAAUACUACCAUCGCAGUAUGUACAGCGGAUAAGUUCUAUCUUAACACCAACGCGAAUGGUGUAGUGAAGACCCAGGUCGGGUAUUCUAAUGAGCUUCCACUGGACCCUAAAGUAAGUGUGCUUGCACAUGUGUCUAUAGUCGACCCUGGCAACGAUCAUCAUAGGACAGUCCCGAACAAUAUGUACACCACCAUGACACGCUUCUGGAGUAUUCGUCCGACUUACACUCUAAAGUCCGUCCUCCGUAUGAUGAUCCUCCUGAUAAAGGAACUUUUAUGCAGGACCGCAUGGUCAACGACCCGAAAUGCCCGCUUCCACGUCACUGCACGGGGACGCCGGUCACUAGAUACGAAUACGACACCGCCAAUGCCGAGGCUCCGGAGGUAUAUUAUUGAUUUGAUCGACUUCCUGUUCCGAGAGCCAGAGGCGGUACGAGCCCAAAAACAAGCGGUUAUAUCCGUAGUCUAUUCCGCCGGCUUCGUGAACGUUCUGGAAUUUACGCGUCAAAACGGCGCCGACAACCUACCAGCCGCCGUGGCAAGGUCAUUCGAUCUUCGUUUGGCGCCCGUUCUUGGGGCGCCGCCGGGUAACGGGAUCGCGAGCUUAGAGUUUUACACAGGCAUGGUUGCACGGGCGGGAUGGCGGGGAACCCACACACACCGCCUCGGUUAUAUUUCCACAAAACGAUCCCCAGGACUCGAUAUACAAUUUGACACGGCUCCGAAUCAUCUGGGUCACCACAGCUGGAUCAUCUUGACCCGAUUCAGGUCGCCCCGAACGUUGCCCAGGAAUAUAUCUCCCGCCUCGACAUUGUCAGAGAUAAAUAAGAUGUACGUUGCUGAAGUACCAAGCCUGGAAUGUCCAAGCUGGUUCGCUUCUAUGCUAAUCCUUUGGAGUGCCAGGUCAAAAUUAUGGCCUGGAUGCAGAGUGCAGGGUGCGGUGGGCGGUCCCUUCAAACAGUCCUUGGCGUGCGGACCUGGAUUCAUUCAAGCCCGACAUCAUCCACUGUGUUUUACGUCUGAGCCAGGAUACAUUACUCAGAAGAAUAACCUUUGGAAACAGCGAUGGCAGGCACUGCCUCGAAUUGCAGAGGUUUUGGCUCUUAGGGAGAGUCCGCGGUCGGAGCUUGCUUAUCAGGAUCAAACAAGGCGUUCCGCUAUCGCAAAUUUGUUGGCUUGUGUGAAGGGUCGUGGGUUAAGAUUAACUGGCCUCUUCCGGUAUCCGAAUAUAGAAUGGAAUUGCAGACAAGAUUUUUGGAUCGCGUGGCAGCUCAUGCAACGUCAGAGUAAGUCAACAUUACGGGACAGAUUGAAUCGCGGUCAAUCCCUAUCAAGAAGGUCGAACUGCGUCGUGGAGGUGAGAGCAUACAUCCGGGGCAGUUCCGAUCACGGGCGUUUAAUCCAUAGCCGAUGCAGAGGAGAACGUGAGUACUGUCACCGAACAAACCCAUCCCGAGUGUACGCGUCAGGCUUUGAUGCAAAUAUGGGUCGGUUUAGAGCUCGUAGCCGCGACCUAACGUCCGUUCUUCGUCCUGUGAUCAAUGACCUAGAAAAUGUCGCGUAUCUAGCCAACUAUGUUCGCUCAACACCUAGCUCACCAGUCCCAUUUUCGCGCCCGCCCGGUCGCGGAGCUACUGGUUCUACUCCUGAAGCGAACAGUGCGCUAAUGAUCCCUUACGCCAAGAUUUUUCAAUUCUCCUCCUACACCCUCGCUCAAAUGUACGGAGAAUUUAGCGCAAAACAUGGUGGCGCGGGAUUCAGCGGUAGCUGUCGCUGGCCUUGA
# """

# p=""

# def findstart(s):
#     for i in range(len(s)-2):
#         codon = s[i]+s[i+1]+s[i+2]
#         if codon == "AUG":
#             return i
            
            
# index=findstart(s)
# for i in range(index,len(s)-2,3):
#     codon = s[i]+s[i+1]+s[i+2]
#     if codon == "UAA" or codon== "UGA" or codon== "UAG":
#         break
#     else:
#         p+=d.get(codon)
        
# print(p)