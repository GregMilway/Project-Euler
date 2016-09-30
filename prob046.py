#Goldbach's conjecture: all odd composite integers can be written as the sum of a prime, and twice a perfect square:

# N = P + 2a**2, for some prime P, and some integer, a

#example given in the problem shows it is true from 9 to 33, however, it has been proven false.
# find the smallest odd composite that cannot be written in this way

import primesieve as ps

def is_square(n):
    return n == int(n**0.5)**2

primes = ps.generate_primes(1000000)

n = 33

while True:
    n += 2
    candidate = True
    for prime in primes:
        rem = n - prime
        if rem > 0 and rem%2 == 0 and is_square(rem/2):
            candidate = False
            break
    if n not in primes and candidate:
        print n
        break
