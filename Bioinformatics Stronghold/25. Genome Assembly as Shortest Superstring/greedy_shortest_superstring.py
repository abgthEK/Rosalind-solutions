import itertools

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

def overlap_len(str1, str2):
	for i in range(len(str1)):
		indx = str1.find(str2[:1], i)
		if indx == -1:
			return 0
		if str2.startswith(str1[indx:]):
			return len(str1) - indx
	
def max_overlap_check(string_list):				 
	seq1, seq2 = None, None							
	max_ov_len = 0	
	for str1, str2 in itertools.combinations(string_list, 2):
		ov_len = overlap_len(str1, str2)
		if ov_len > max_ov_len:
			seq1, seq2 = str1, str2
			max_ov_len = ov_len
	return seq1, seq2, max_ov_len

def shortest_superstring(string_list):
	seq1, seq2, ov_len = max_overlap_check(string_list)
	#print(ov_len)
	while ov_len > 0:
		string_list.remove(seq1)
		string_list.remove(seq2)
		string_list.append(seq1 + seq2[ov_len:])
		seq1, seq2, ov_len = max_overlap_check(string_list)
		#print(ov_len)
	return ''.join(string_list)

print(shortest_superstring(string_list))
print(len(shortest_superstring(string_list)))