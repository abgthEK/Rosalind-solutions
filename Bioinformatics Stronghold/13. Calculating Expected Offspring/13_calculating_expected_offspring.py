'''
Problem:

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1

Sample Output
3.5
'''

f = open('rosalind_iev.txt', 'r')

lines = f.read().splitlines()[0].split()

#genotype pairing
gp1 = int(lines[0]) 	#AA - AA
gp2 = int(lines[1])		#AA - Aa
gp3 = int(lines[2])		#AA	- aa
gp4 = int(lines[3])		#Aa - Aa
gp5 = int(lines[4])		#Aa - aa
gp6 = int(lines[5])	    #aa - aa

exp_offspring = 2*(gp1*1 + gp2*1 + gp3*1 + gp4*0.75 + gp5*0.50 + gp6*0)

print(exp_offspring)