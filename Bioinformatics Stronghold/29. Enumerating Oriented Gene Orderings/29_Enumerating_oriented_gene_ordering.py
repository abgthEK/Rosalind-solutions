'''
Problem:

Given: A positive integer n ≤ 6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

Sample Dataset
2

Sample Output
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1

'''

from itertools import permutations

f = open('rosalind_sign.txt','r')

n = int(f.read())

nlist = [x for x in list(range(-n, n+1)) if x!=0]

permutation_list = []

for perm in list(permutations(nlist, n)):
    perm_check = [abs(x) for x in perm]
    if any(perm_check.count(ele) > 1 for ele in perm_check) is False:
        permutation_list.append(perm)

print(len(permutation_list))

for signed_perm in permutation_list:
    print(*signed_perm)