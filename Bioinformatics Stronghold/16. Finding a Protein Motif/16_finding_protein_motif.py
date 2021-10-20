'''
Problem: Finding N-glycosylation motif - N{P}[ST]{P}

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
'''

from Bio import SeqIO
from io import StringIO
import requests

f = open('rosalind_mprt.txt', 'r')
lines = f.read().splitlines()
url = ""
fasta_list = []
fasta_seq = ""

def get_fasta(url):
	data = requests.get(url).text
	fasta_iterator = SeqIO.parse(StringIO(data), "fasta")
	for seq in fasta_iterator:
		fasta_list = seq.format("fasta").splitlines()
		return ''.join(fasta_list[1:len(fasta_list)])

for i in range(len(lines)):
	url = "http://www.uniprot.org/uniprot/"+lines[i]+".fasta"
	fasta_seq = get_fasta(url)
	list_motif = []
	count = 0
	for j in range(0, len(fasta_seq)-3):
		four_mer = fasta_seq[j:j+4]
		if four_mer[0] == 'N':
			if four_mer[1] != 'P':
				if four_mer[2] == 'S' or four_mer[2] == 'T':
					if four_mer[3] != 'P':
						count += 1
						list_motif.append(j+1)
	if count > 0:
		print(lines[i])
		print(*list_motif)