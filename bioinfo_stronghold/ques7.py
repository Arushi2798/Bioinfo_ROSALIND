"""Given: Three positive integers k, m, and n, representing a population containing k+m+n
organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n
are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate."""

import random
k,m,n=2,2,2
p=k+m+n
parents=[]
for j in range(k):
    parents.append("AA")
for j in range(m):
    parents.append("Aa")
for j in range(n):
    parents.append("aa")
# print(parents)


while True:
    ind1=random.randint(0,p-1)
    ind2=random.randint(0,p-1)
    if ind1 != ind2:
        break
a=parents[ind1]
b=parents[ind2]
# print(ind1,ind2)
# print(a,b)

#no of dominant allel
dom= k*2 + m
#no of recessive allel
rec= m+n*2
#parents could be AA, Aa, aa
#in case of homozygous dominant progeny AA
if a==b:
    pass
#in case of heterozygous progeny Aa

#in case of homozygous recessive progeny aa