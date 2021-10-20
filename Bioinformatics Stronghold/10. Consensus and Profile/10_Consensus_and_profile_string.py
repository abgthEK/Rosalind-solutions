'''
Problem:

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

import numpy as np
import pandas as pd

f = open('rosalind_cons.txt', 'r')

lines = f.read().splitlines()

dna_string_lines = [(lines[i]) for i in range(0, len(lines))]

dna_string = []
dna_matrix = []
dna_line = []

for z in range(1, len(dna_string_lines)):
	if dna_string_lines[z].startswith(">"):
		dna_string.append("".join(dna_line))
		dna_line = []
	else:
		dna_line.append(dna_string_lines[z])
	if z == len(dna_string_lines)-1:
		dna_string.append("".join(dna_line))

for j in dna_string:
	a1 = np.array(list(j))
	dna_matrix.append(a1)

dna_matrix = np.asarray(dna_matrix)
	
dna_df = pd.DataFrame(dna_matrix)

A_count = []
C_count = []
G_count = []
T_count = []
consensus_string = []

for k in range(len(dna_matrix[0])):
	consensus = []
	consensus.append(dna_df[k].str.count('A').sum())
	consensus.append(dna_df[k].str.count('C').sum())
	consensus.append(dna_df[k].str.count('G').sum())
	consensus.append(dna_df[k].str.count('T').sum())
	A_count.append(dna_df[k].str.count('A').sum())
	C_count.append(dna_df[k].str.count('C').sum())
	G_count.append(dna_df[k].str.count('G').sum())
	T_count.append(dna_df[k].str.count('T').sum())
	if consensus.index(max(consensus)) == 0:
		consensus_string += 'A'
	if consensus.index(max(consensus)) == 1:
		consensus_string += 'C'
	if consensus.index(max(consensus)) == 2:
		consensus_string += 'G'
	if consensus.index(max(consensus)) == 3:
		consensus_string += 'T'

print("".join(consensus_string))
print("A: {}".format(' '.join(map(str, A_count))))
print("C: {}".format(' '.join(map(str, C_count))))
print("G: {}".format(' '.join(map(str, G_count))))
print("T: {}".format(' '.join(map(str, T_count))))