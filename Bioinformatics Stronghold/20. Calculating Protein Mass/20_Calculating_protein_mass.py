'''
Problem:

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Sample Dataset
SKADYEK

Sample Output
821.392
'''

f = open('rosalind_prtm.txt', 'r')
g = open('monoisotopic_mass.txt' , 'r')

lines = f.read().splitlines()
seq = ''.join(lines) 

mass = g.read().splitlines()
mono_mass_dict = {}
total_mass = 0

for line in mass:
    line_m = line.split()
    mono_mass_dict[line_m[0]] = float(line_m[1])

for aa in seq:
    total_mass += mono_mass_dict[aa]

print(total_mass)