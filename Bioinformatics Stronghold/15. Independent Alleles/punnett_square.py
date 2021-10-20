#Punnett_square

from itertools import product
square = list(product('Aa', 'Bb', repeat=2))
print([''.join(sorted(x, key=lambda x:x.lower())) for x in square])