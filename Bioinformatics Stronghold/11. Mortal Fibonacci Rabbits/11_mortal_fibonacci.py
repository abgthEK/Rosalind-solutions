'''
Problem:

Given: Positive integers n ≤ 100 and m ≤ 20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4
'''

f = open('rosalind_fibd.txt', 'r')
values = f.read().split()

n = int(values[0])
m = int(values[1])
dict = {}

def fibonacci(i, pop):	#normal fibonacci step --> adding new life when n<m
	val = i
	if val in dict:
		return dict[val]
	else:
		fib = pop[i-1] + pop[i-2]
		dict[val] =  fib
		return fib

def mortal(n, m):
	population = [1, 1, 2] #3rd gen population list
	for i in range(3, n):
		calc_population = fibonacci(i, population) 
		if i == m:
			calc_population = calc_population-1  # accounting death into list
		elif i > m:
			calc_population -= population[i-m-1] # when n>m, F(n) = F(n-1) + F(n-2) - F(n-(m+1)) 
		population.append(calc_population)
	print(population[n-1])

mortal(n, m)