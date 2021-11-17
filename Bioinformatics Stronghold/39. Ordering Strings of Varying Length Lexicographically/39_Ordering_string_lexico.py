'''
Problem:

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

Sample Dataset
D N A
3

Sample Output
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA

'''
import itertools
from itertools import product

f = open('rosalind_lexv.txt', 'r')
chars = f.read().split()

alphb = chars[:-1]
n = int(chars[-1])

def all_comb(alph, n):
    comb_lst = []
    for i in range(1, n+1):
        for string in product(alph, repeat=i):
             comb_lst.append(''.join(string))
    return comb_lst

def order_lex(comb, alph):
    return sorted(comb, key=lambda word: [alph.index(c) for c in word])
    

comb_list = all_comb(alphb, n)
ord_list = order_lex(comb_list, alphb)

print(*ord_list, sep='\n')

