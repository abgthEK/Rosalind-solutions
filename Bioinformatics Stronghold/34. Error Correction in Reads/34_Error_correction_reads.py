'''
Problem:

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. 

Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

Sample Dataset
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC

Sample Output
TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA

'''
from collections import Counter

f = open('rosalind_corr.txt', 'r')

read_list = [seq for seq in f.read().split() if '>' not in seq]

def rev_complement(seq):
    for e in range(len(seq)):
        if seq[e] == 'A':
            seq[e] = 'T'
        elif seq[e] == 'T':
            seq[e] = 'A'
        elif seq[e] == 'C':
            seq[e] = 'G'
        elif seq[e] == 'G':
            seq[e] = 'C'
    rev_compl = ''.join(reversed(seq))
    return rev_compl

def error_check(seq_list, count):
    correct = []
    error = []
    for seq in count:
        if count[seq] >= 2:
            correct.append(seq)
        elif seq in read_list:
            error.append(seq)
    return correct, error

def hamm_dist(seq1, seq2):
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist 

def error_correction(error, correct):
    new_read = []
    old_read = []
    for seq1 in error:
        for seq2 in correct:
            if hamm_dist(seq1, seq2) == 1:
                old_read.append(seq1)
                new_read.append(seq2)
    return old_read, new_read

rev_comp_list = [rev_complement(list(read)) for read in read_list]
seq_count = Counter(read_list+rev_comp_list)

correct, error = error_check(read_list, seq_count)
old_read, new_read = error_correction(error, correct)

for i in range(len(old_read)):
    print('{}->{}'.format(old_read[i], new_read[i]))

