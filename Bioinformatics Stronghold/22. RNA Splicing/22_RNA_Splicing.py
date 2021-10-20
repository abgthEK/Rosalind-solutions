'''
Problem:

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
'''

f = open('rosalind_splc.txt', 'r')

lines = f.read().splitlines()
dnaseq = []
sequences = []
rna_dict = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
			'UAU':'Y', 'UAC':'Y', 'UAA':'', 'UAG':'', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
			'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

def rna_prot(seq):
    prot = []
    list_cod = [(seq[t:t+3]) for t in range(0, len(seq), 3)]
    for w in range(len(list_cod)):
        prot.append(rna_dict[list_cod[w]])
    return ''.join(prot)

def intron_remv(intrn, dna):
    newseq = dna
    for intr in intrn:
        newseq = newseq.replace(intr, "")
    return newseq

for seq in lines:
    if '>' in seq:
        if len(sequences) != 0:
            dnaseq.append(''.join(sequences))
        sequences = []
    else:
        sequences.append(seq)
    if seq == lines[-1]:
        dnaseq.append(''.join(sequences))

dnastring = dnaseq[0]
introns = dnaseq[1:]

rna_string =  intron_remv(introns, dnastring).replace("T", "U")

print(rna_prot(rna_string))    