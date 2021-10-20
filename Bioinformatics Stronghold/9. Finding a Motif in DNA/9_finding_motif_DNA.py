'''
Problem:

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10

'''

f = open('rosalind_subs.txt', 'r')

lines = list(f.read().splitlines())

s1 = lines[0]
s2 = lines[1]
list_motif = []

for i in range(len(s1)-len(s2)):
	s3 = s1[i:i+len(s2)]
	if s3 == s2:
		list_motif.append(i+1)
		
print(*list_motif)