"""Given: Three positive integers k, m, and n, representing a population containing k+m+n
organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n
are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate."""

import random
k,m,n=2,2,2
p=k+m+n

indiv=[]
indiv.append(random.randint(0,p))
indiv.append(random.randint(0,p))

# print(indiv)
#in case of homozygous dominant
#in case of heterozygous
#in case of homozygous recessive