'''
Problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21

'''

f = open('rosalind_dna.txt', 'r')

lines = f.readlines()

A = lines[0].count('A')
G = lines[0].count('G')
C = lines[0].count('C')
T = lines[0].count('T')

print('{} {} {} {}'.format(A, C, G, T))