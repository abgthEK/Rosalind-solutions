'''
Problem:

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
'''

f = open('rosalind_prot.txt', 'r')

lines = list(f.read().splitlines())

list_prot = []
list_rna = [(lines[0][i:i+3]) for i in range(0, len(lines[0]), 3)]

rna_dict = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
			'UAU':'Y', 'UAC':'Y', 'UAA':'', 'UAG':'', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
			'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

for j in range(len(list_rna)):
	S = rna_dict[list_rna[j]]
	list_prot.append(S)

print(''.join(list_prot))