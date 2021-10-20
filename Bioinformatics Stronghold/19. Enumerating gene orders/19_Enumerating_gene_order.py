'''
Problem:

A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

from itertools import permutations
import math as mp

f = open('rosalind_perm.txt', 'r')

n = int(f.read())

permutations_list = list(permutations(range(1, n+1)))
no_perm = mp.factorial(n)

print(no_perm)
for i in range(no_perm):
    print(*permutations_list[i])