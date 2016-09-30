#which prime, below 1000000 can be written as the sum of the most consecutive primes?

#
#generating all primes below 1000000 takes no time at all

import primesieve as ps
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return (pos if pos != hi and a[pos] == x else -1)

limit = 1000000
primes = ps.generate_primes(limit)
prime_sum = [0]*(len(primes)+1)
primecount = 0
max_prime = 0

for i in xrange(len(primes)):
    prime_sum[i+1] = prime_sum[i]+primes[i]

i = 0
while i < len(prime_sum):
    for j in xrange(i-(primecount-1),-1,-1):
        if prime_sum[i]-prime_sum[j] > limit:
            break
        if binary_search(primes, (prime_sum[i]-prime_sum[j])) >= 0:
            primecount = i-j
            max_prime = prime_sum[i]-prime_sum[j]
    i += 1

print max_prime
