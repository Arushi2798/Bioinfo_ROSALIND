"""A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π)
 and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn
 represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn
 that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair)."""

import time

# a,b=1,1
# n=29
# k=4
# # print(a,b,end=' ')

# for i in range(n-2):
#     c=a*k+b
#     a=b
#     b=c
#     # print(c,end=" ")
# print(c)

##another attempt

# def fibo(n,k):
#     prev1,prev2=1,1
#     for i in range(n-2):
#         prev1,prev2=prev2 , prev1*k + prev2
#     return prev2
    
# print(fibo(n,k))

##another attempt
# start=time.time()
# # print(start)
# def rabbit(n,k):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     return(rabbit(n-1,k) + rabbit(n-2,k) *k)

# print(rabbit(40,2))
# print(time.time()-start)


##DP attempt

memo={}
start=time.time()
# print(start)
def rabbit(n,k):
    #args=(n,k)
    if n in memo: #give args instead of n
        return memo[n] #give memo[args] instead of memo[n]
    
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        ans=(rabbit(n-1,k) + rabbit(n-2,k) *k)
    memo[n]=ans#give memo[args] instead of memo[n]
    return ans

print(rabbit(40,2))
# print(time.time()-start)

# print(memo)