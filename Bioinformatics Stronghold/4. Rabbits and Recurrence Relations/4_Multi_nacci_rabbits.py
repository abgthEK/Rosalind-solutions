'''
Problem:

Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset
5 3

Sample Output
19
'''
f = open('rosalind_fib.txt', 'r')
values = f.read().split()

dict = {}
n = int(values[0])
k = int(values[1])

def multi(n, k):
	val = (n, k)
	if val in dict:
		return dict[val]
	elif n <= 2:
		return 1
	elif n >= 3:
		ans = multi(n-1, k) + k*multi(n-2, k)
	dict[val] = ans
	return ans

print(multi(n, k))