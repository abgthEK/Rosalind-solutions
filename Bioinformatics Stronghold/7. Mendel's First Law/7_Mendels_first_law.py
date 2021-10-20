'''
Problem:

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
2 2 2

Sample Output
0.78333

'''
f = open('rosalind_iprb.txt', 'r')
values = f.read().split()

import random

k = int(values[0])
m = int(values[1])
n = int(values[2])

t = float(k+m+n)

prob = 0
p = 0
num_iter = 1000000

hom_dom = [2]*k # AA = 2
hom_rec = [0]*n # aa = 0
het_dom = [1]*m # Aa = 1

org_list = hom_dom+hom_rec+het_dom
for i in range(num_iter):
	sel = random.sample(org_list, 2)
	if sel[0]+sel[1] > 2 or 2 in sel:
		prob+=1
	if sel[0]+sel[1] == 2 and 2 not in sel:
		prob+= 0.75
	if sel[0]+sel[1] == 1:
		prob+= 0.50
	if sel[0]+sel[1] == 0:
		prob+=0

print(prob/float(num_iter))

#Other Solution

d = float((k + (m/2))/t) #first parent donates a dominant allele
l = float(((m/2)/t)*(k+((m-1)/2))/(t-1)) #probability that the first parent is heterozygous and does not donate, but the child receives the trait from the other parent
n = float((n/t)*(k+m/2)/(t-1)) #probability that the first parent is homozygous recessive and the child has the trait.

p = d+l+n
print(p)