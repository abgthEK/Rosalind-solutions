'''
Problem:

Given: A positive integer n (3≤n≤10000).

Return: The number of internal nodes of any unrooted binary tree having n leaves.

Sample Dataset
4

Sample Output
2

'''

f = open('rosalind_inod.txt', 'r')

n = int(f.read())

print(n-2)