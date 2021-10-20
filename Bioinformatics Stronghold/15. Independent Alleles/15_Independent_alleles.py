'''
Problem:

Given: Two positive integers k (k ≤ 7) and N (N ≤ 2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1

Sample Output
0.684
'''

import math as mt

f = open('rosalind_lia.txt', 'r')
values = f.read().split()

k = int(values[0])
N = int(values[1])

Tot_pop = 2**k

def prob(k, N):
	total = 0
	for i in range(N, Tot_pop):
		probability = (mt.factorial(Tot_pop) / (mt.factorial(Tot_pop - i) * mt.factorial(i))) * (0.25**i) * (0.75**(Tot_pop - i)) #AaBb probability = 0.25
		total += probability
	print(total)

prob(k, N)