'''
Problem:

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

Sample Output
1.21428571429

'''

f = open('rosalind_tran.txt', 'r')

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

def TI_TV_ratio(seq1, seq2): 
    transition, transversion = 0, 0
    for i in range(len(seq1)):
        if seq1[i] == 'A':
            if seq2[i] == 'G':
                transition +=1
            if seq2[i] in ['C', 'T']:
                transversion +=1
        if seq1[i] == 'G':
            if seq2[i] == 'A':
                transition +=1
            if seq2[i] in ['C', 'T']:
                transversion +=1
        if seq1[i] == 'C':
            if seq2[i] == 'T':
                transition +=1
            if seq2[i] in ['A', 'G']:
                transversion +=1
        if seq1[i] == 'T':
            if seq2[i] == 'C':
                transition +=1
            if seq2[i] in ['A', 'G']:
                transversion +=1
    return float(transition/ transversion)

seq1, seq2 = dna_line_split(lines)
ratio = TI_TV_ratio(seq1, seq2)

print(ratio)