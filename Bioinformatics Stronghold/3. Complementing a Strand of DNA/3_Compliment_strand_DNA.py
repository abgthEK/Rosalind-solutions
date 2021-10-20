'''
Problem:

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT
'''

f = open('rosalind_revc.txt', 'r')

lines = f.readlines()

S = list(lines[0])

for i in range(len(S)):
	if S[i] == 'A':
		S[i] = 'T'
	elif S[i] == 'T':
		S[i] = 'A'	
	elif S[i] == 'C':
		S[i] = 'G'
	elif S[i] == 'G':
		S[i] = 'C'	

print("".join(reversed(S)))