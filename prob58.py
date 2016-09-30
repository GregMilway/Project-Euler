# for an anti-clockwise spiral, find the smallest grid size for which the ratio of primes on the diagonals falls below 10%

# for a given grid size n*n, there are 2*n-1 diagonal elements.
# for each grid size, (n is odd), the four new diagonal elements are (last corner) + k*(n-1) for k = 1,2,3,4

import primesieve as ps
primeIter = ps.Iterator()

def is_prime(n):
    if n < 2:
        return False
    else:
        primeIter.skipto(n-1)
        return primeIter.next_prime() == n

def count_primes(lst):
    return len([elem for elem in lst if is_prime(elem)])

n = 1           #size of the grid
corners = [1]   #the corner elements of the grid
prime_count = 0
while True:
    n += 2
    lastcorner = corners[-1]
    corners = [lastcorner+k*(n-1) for k in range(1,5)]
    prime_count += count_primes(corners)
    if prime_count / (2.0*n-1.0) < 0.1:
        break

print n
