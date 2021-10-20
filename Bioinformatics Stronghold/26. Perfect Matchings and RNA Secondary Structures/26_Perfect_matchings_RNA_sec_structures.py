'''
Problem:

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

Sample Dataset
>Rosalind_23
AGCUAGUCAU

Sample Output
12

'''

from math import factorial

f = open('rosalind_pmch.txt', 'r')

lines = f.read().splitlines()
seq = lines[1]+lines[2]

def possible_perfect_matchings(seq):
    nA = seq.count('A')
    nC = seq.count('C')
    return factorial(nA)*factorial(nC)

print(possible_perfect_matchings(seq))