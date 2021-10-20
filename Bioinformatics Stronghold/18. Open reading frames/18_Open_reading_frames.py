'''
Problem:

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

f = open('rosalind_orf.txt', 'r')

lines = f.read().splitlines()
sequence = ''.join(lines[1:])

start_codon = 'AUG'
stop_codon = ['UGA', 'UAA', 'UAG']
rna_dict = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
			'UAU':'Y', 'UAC':'Y', 'UAA':'', 'UAG':'', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
			'UGU':'C', 'UGC':'C', 'UGA':'', 'UGG':'W', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

def dna2rna(dnaseq):
    return dnaseq.replace("T", "U")

def rev_complement(dnaseq):
    for e in range(len(dnaseq)):
        if dnaseq[e] == 'A':
            dnaseq[e] = 'T'
        elif dnaseq[e] == 'T':
            dnaseq[e] = 'A'
        elif dnaseq[e] == 'C':
            dnaseq[e] = 'G'
        elif dnaseq[e] == 'G':
            dnaseq[e] = 'C'
    rev_rna = ''.join(reversed(dnaseq))
    return rev_rna.replace("T", "U")

def rna_prot(seq):
    prot = []
    list_cod = [(seq[t:t+3]) for t in range(0, len(seq), 3)]
    for w in range(len(list_cod)):
        prot.append(rna_dict[list_cod[w]])
    return ''.join(prot)
        
RNA_seq, rev_RNA_seq = dna2rna(sequence), rev_complement(list(sequence))

orf_list = []

def orf_read(seq):
    start_codon_index = []
    stop_codon_index = []
    for m in range(len(seq)-2):
        codon = seq[m:m+3]
        if codon == start_codon:
            start_codon_index.append(m)
        if codon in stop_codon:
            stop_codon_index.append(m)

    for k in start_codon_index:
        for l in stop_codon_index:
            if k < l and l - k >= 3 and len(seq[k:l])%3 == 0:
                orf_list.append(seq[k:l])
                break
    return orf_list

orf_list = orf_read(RNA_seq) + orf_read(rev_RNA_seq)

uniq_orf_list = list(set(orf_list))

for cod in uniq_orf_list:
    print(rna_prot(cod))