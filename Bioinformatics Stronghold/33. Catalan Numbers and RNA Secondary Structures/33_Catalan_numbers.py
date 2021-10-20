'''
Problem:

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

Sample Dataset
>Rosalind_57
AUAU

Sample Output
2

'''

f = open('rosalind_cat.txt', 'r')

seq = ''.join(f.read().splitlines()[1:])

