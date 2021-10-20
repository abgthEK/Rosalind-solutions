'''
Problem:

Given: A collection of k (k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
'''
f = open('rosalind_lcsm.txt', 'r')
lines = f.read().splitlines()

dna_string = []
dna_line = []

for z in range(0, len(lines)):
	if lines[z].startswith(">"):
		if z != 0:
			dna_string.append("".join(dna_line))
			dna_line = []
	else:
		dna_line.append(lines[z])
	if z == len(lines)-1:
		dna_string.append("".join(dna_line))
  
def subsearch(sublist):
	strings = sublist[0]
	l = len(strings)
	sub_long = ""
	for i in range(l):
		for j in range(i+1, l+1):
			sub = strings[i:j]
			k = 1
			for k in range(1, len(sublist)):
				if sub not in sublist[k]:
					break
			if (k + 1 == len(sublist) and len(sub_long) < len(sub)):
				sub_long = sub
	return sub_long
 
substring = subsearch(dna_string)
print(substring)