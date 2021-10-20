'''
Problem:

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
'''

f = open('rosalind_hamm.txt', 'r')

lines = f.read().splitlines()
count = 0

seq1 = list(lines[0])
seq2 = list(lines[1])

for i in range(len(seq1)):
	if seq1[i] != seq2[i]:
		count += 1

print(count)