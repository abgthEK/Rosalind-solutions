'''
Problem:

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
'''

f = open('rosalind_revp.txt', 'r')

lines = f.read().splitlines()
sequence = ''.join(lines[1:])

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

len_range = list(range(4,13))

for i in range(len(sequence)):
    for j in range(i+1, len(sequence)+1):
        temp_str = sequence[i:j]
        if len(temp_str) in len_range:
            if temp_str == rev_complement(list(temp_str)):
                print('{} {}'.format(i+1, len(temp_str)))