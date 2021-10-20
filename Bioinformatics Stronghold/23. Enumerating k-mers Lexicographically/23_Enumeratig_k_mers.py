'''
Problem:

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2

Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
'''

from itertools import product

f = open('rosalind_lexf.txt', 'r')

lines = f.read().splitlines()

alph_list = list(lines[0].replace(" ", ""))
k_len = int(lines[1])

for string in product(alph_list, repeat=k_len):
    print(''.join(string))