'''
Problem:

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output
Rosalind_0808
60.919540
'''

f = open('rosalind_gc.txt', 'r')

lines = f.readlines()

count_id = []
gc_percent = []
gc_line = leng = 0

def line_count(line):
	l = len(line)
	count = line.count('G')+line.count('C')
	return l, count
	
for i in range(len(lines)):
	if '>' in lines[i]:
		count_id.append(lines[i].replace(">", "").rstrip())
		if gc_line != 0:
			gc_percent.append((gc_line*100)/float(leng))
			gc_line = 0
			leng = 0
	else:
		lg, gc_l = line_count(lines[i].rstrip())
		leng += lg
		gc_line += gc_l
	if i == len(lines)-1:
		gc_percent.append(float(gc_line*100)/float(leng))

max_count_id = count_id[gc_percent.index(max(gc_percent))]
max_count =  max(gc_percent)
print(max_count_id)
print(max_count)