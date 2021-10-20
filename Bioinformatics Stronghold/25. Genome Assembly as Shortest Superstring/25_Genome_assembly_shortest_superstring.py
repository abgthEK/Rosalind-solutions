'''
Problem:

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC

'''

f = open('rosalind_long.txt', 'r')

lines = f.read().splitlines()
string_list = []
seq_line = []

for z in range(0, len(lines)):
	if lines[z].startswith(">"):
		if z != 0:
			string_list.append("".join(seq_line))
		seq_line = []
	else:
		seq_line.append(lines[z])
	if z == len(lines)-1:
		string_list.append("".join(seq_line))

superstring = string_list[0]

def overlap_check(string_list, superstring):
    for str1 in string_list:
        for indx in range(len(str1)//2):
            overlap = len(str1) - indx
            if superstring.startswith(str1[indx:]):
                return str1, str1[:indx] + superstring
            if superstring.endswith(str1[:overlap]):
                return str1, superstring + str1[overlap:]

def shortest_superstring(string_list, superstring):
    while True:
        seq1, superstring = overlap_check(string_list, superstring)
        string_list.remove(seq1)
        if len(string_list) == 0:
            return superstring, len(superstring)


shortest_ss, ss_len = shortest_superstring(string_list, superstring)

print(shortest_ss)
#print(ss_len)