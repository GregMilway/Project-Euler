#find the smallest sum of a set of 5 primes, that when any two are concatenated, in any order, they make a prime.

#first, generate a nice large list of primes to choose from:

import primesieve as ps
from time import time

primes = ps.generate_primes(10000)
primeIter = ps.Iterator()

def is_prime(n):
    primeIter.skipto(n+1)
    return primeIter.previous_prime() == n

def make_prime(a,b):
    return int( str(a) + str(b) )

def get_pairs(a):
    #returns set of primes that can be concatenated with primes[a] either way round to make new primes
    pairs = set()
    for b in xrange(a+1,len(primes)):
         if is_prime(make_prime(primes[a],primes[b])) and is_prime(make_prime(primes[b],primes[a])):
             pairs.add(primes[b])
    return pairs

start = time()
prime_pairs = []
for i in range(len(primes)):
    prime_set = get_pairs(i)
    if len(prime_set) > 0:
        prime_pairs.append((primes[i],prime_set))
end = time()
print len(prime_pairs)
print end-start

