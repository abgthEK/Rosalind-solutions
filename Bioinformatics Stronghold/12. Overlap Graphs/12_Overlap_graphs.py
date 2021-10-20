'''
Problem:

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''

f = open('rosalind_grph.txt', 'r')

t = int(input("overlap length: ")) #Here t = 3

lines = f.read().splitlines()

dna_string = []
dna_line = []
count_id = []

for z in range(0, len(lines)):
	if '>' in lines[z]:
		count_id.append(lines[z].replace(">", ""))
	if lines[z].startswith(">"):
		if z != 0:
			dna_string.append("".join(dna_line))
		dna_line = []
	else:
		dna_line.append(lines[z])
	if z == len(lines)-1:
		dna_string.append("".join(dna_line))

for i in range(len(dna_string)):
	str1 = dna_string[i][0:t]
	for j in range(len(dna_string)):
		if i != j:
			str2 = dna_string[j][-t:]
			if str1 == str2:
				print('{} {}'.format(count_id[j], count_id[i]))