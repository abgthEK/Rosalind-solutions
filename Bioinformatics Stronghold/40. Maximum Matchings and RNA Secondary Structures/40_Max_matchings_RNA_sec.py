'''
Problem:

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.

Sample Dataset
>Rosalind_92
AUGCUUC

Sample Output
6

'''
from math import factorial

f = open('rosalind_mmch.txt', 'r')

lines = f.read().splitlines()
seq = ''.join(lines[1:])

def max_matchings(seq):
    nA = seq.count('A')
    nC = seq.count('C')
    nG = seq.count('G')
    nU = seq.count('U')
    return factorial(max(nA, nU))//factorial(max(nA, nU) - min(nA, nU)), factorial(max(nG, nC))//factorial(max(nG, nC) - min(nG, nC))

nAU, nGC = max_matchings(seq)

print(int(nAU*nGC))


