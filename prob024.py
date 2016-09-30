# find the 1 millionth lexicographic permutation of the numbers 0,1,2,3,4,5,6,7,8,9.
# 1) create all permutations of digits.
# 2) sort list of permutations
# 3) find 1 millionth permutation
from itertools import permutations
numchar = '0123456789'

perms = list(permutations(numchar))

print perms[999999]
