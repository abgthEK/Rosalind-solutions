'''
Problem:

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample Output
3 8 10

'''

f = open('rosalind_sseq.txt', 'r')

lines = f.read().splitlines()

def dna_line_split(lines):
    string_list = []
    seq_line = []
    for z in range(0, len(lines)):
	    if lines[z].startswith(">"):
		    if z != 0:
			    string_list.append("".join(seq_line))
		    seq_line = []
	    else:
		    seq_line.append(lines[z])
	    if z == len(lines)-1:
		    string_list.append("".join(seq_line))
    return string_list[0], string_list[1]

def get_indices(seq1, seq2):
	indices = []
	for seq in seq2:
		indices.append([index+1 for index, ele in enumerate(seq1) if ele == seq])
	return indices

def subseq(indice_list):
	subseq = []
	for indices in indice_list:
		if len(subseq) == 0:
			subseq.append(min(indices))
			continue
		for indx in indices:
			if indx > subseq[len(subseq)-1]:
				subseq.append(indx)
				break
	return subseq

seq1, seq2 = dna_line_split(lines)
indice_list = get_indices(seq1, seq2)
subseq_indices =  subseq(indice_list)

print(*subseq_indices)