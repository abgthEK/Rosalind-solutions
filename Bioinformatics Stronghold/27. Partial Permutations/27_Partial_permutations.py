'''
Problem:

Given: Positive integers n and k such that 100 ≥ n > 0 and 10 ≥ k > 0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

Sample Dataset
21 7

Sample Output
51200

'''

from math import factorial

f = open('rosalind_pper.txt', 'r')
values = f.read().split()

n = int(values[0])
k = int(values[1])

def partial_perm(n, k):
    return int(factorial(n)/factorial(n-k))

print(partial_perm(n, k)%1000000)