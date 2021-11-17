'''
Problem:

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)

Sample Dataset
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA

Sample Output
AACTGG

'''
f = open('rosalind_lcsq.txt', 'r')

lines = f.read().splitlines()

def seq_line_split(lines):
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
    return string_list[0], string_list[1]

def long_csq(s1, s2, m, n):
    mat = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    
    indx = mat[m][n]

    lcsq = [""] * (indx+1)
    lcsq[indx] = ""

    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcsq[indx-1] = s1[i-1]
            i -= 1
            j -= 1
            indx -= 1

        elif mat[i-1][j] > mat[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcsq)

seq1, seq2 = seq_line_split(lines)
lcsq = long_csq(seq1, seq2, len(seq1), len(seq2))

print(lcsq)

