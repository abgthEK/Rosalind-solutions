'''
Problem:

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

Sample Dataset
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783

Sample Output
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

'''

from math import log10

f = open('rosalind_prob.txt', 'r')

lines = f.read().splitlines()

seq = lines[0]
arrA = [float(x) for x in lines[1].split()]

nAT, nGC = 0, 0
log10_list = []

for base in seq:
    if base == 'A' or base == 'T':
        nAT += 1
    if base == 'G' or base == 'C':
        nGC += 1

for prob in arrA:
    new_prob = (((1-prob)/2)**nAT)*((prob/2)**nGC)
    log10_list.append(round(log10(new_prob), 4))

print(*log10_list)