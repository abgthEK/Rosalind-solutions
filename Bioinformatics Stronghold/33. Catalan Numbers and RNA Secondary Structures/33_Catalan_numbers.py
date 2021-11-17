'''
Problem:

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

Sample Dataset
>Rosalind_57
AUAU

Sample Output
2

'''

from itertools import product

f = open('rosalind_cat.txt', 'r')

rna_seq = ''.join(f.read().splitlines()[1:])

rna = ['A', 'U', 'C', 'G', ''] + [''.join(i) for i in product(['A', 'U', 'C', 'G'], repeat=2)] 
seq_dict = {}

for aa in rna:
    if aa in ['AU', 'UA', 'GC', 'CG', '']:
        seq_dict[aa] = 1
    else:
        seq_dict[aa] = 0

print(seq_dict)

def count_sec_struct(seq):    
    if seq not in seq_dict:
        curr_seq = []
        for k in range(1, len(seq), 2):
            left = count_sec_struct(seq[1:k])
            right = count_sec_struct(seq[k+1:])
            curr = left * seq_dict[seq[0]+seq[k]] * right
            curr_seq.append(curr)
        seq_dict[seq] = sum(curr_seq)
    return seq_dict[seq]

print(count_sec_struct(rna_seq)%1000000)

