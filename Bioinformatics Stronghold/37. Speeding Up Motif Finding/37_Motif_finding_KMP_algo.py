'''
Problem:

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.

Sample Dataset
>Rosalind_87
CAGCATGGTATCACAGCAGAG

Sample Output
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0

'''
f = open('rosalind_kmp.txt', 'r')

lines = f.read().splitlines()
seq = ''.join(lines[1:])

fail_arr = [0]*len(seq)

idx = 0

for i in range(2, len(seq)+1):
    while idx > 0 and seq[idx] != seq[i-1]:
        idx = fail_arr[idx-1]
    if seq[idx] == seq[i-1]:
        idx += 1
    fail_arr[i-1] = idx

print(*fail_arr)
