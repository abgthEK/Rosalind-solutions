'''
Problem:

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA

Sample Output
12
'''

f = open('rosalind_mrna.txt', 'r')

lines = f.read().splitlines()

dict = {'F':2, 'L':6, 'I':3, 'S':6, 'P':4, 'T':4, 'A':4, 'Y':2, 'H':2, 'Q':2, 'N':2, 'K':2, 'D':2, 'E':2, #Number of possible codons per aa
        'C':2, 'W':1, 'R':6, 'G':4, 'M':1, 'V':4}

prob = 3    #including 3 possible stop codon ['UAA', 'UGA', 'UAG']

for seq in lines[0]:
    prob *= dict[seq]
    
print(prob%1000000)