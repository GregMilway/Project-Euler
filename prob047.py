# find the first four consecutive integers with four distinct prime factors,e.g.:
# n     =   prime*prime*prime*prime
# n+1   =   prime*prime*prime*prime
# n+2   =   ...
# n+3   =   ...

# First, find an integer with 4 distinct prime factors,
# second, check if consecutive integers also have 4 distinct prime factors
# if so, done, if not, check for the next integer with 4 distinct prime factors
from bisect import bisect_left
from primesieve import generate_primes
def factors(n):
    factset = set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
    factset.discard(1)
    factset.discard(n)
    return factset

__primes = generate_primes(31622)
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    f = 31627
    while f < limit:
        if n%f == 0 or n%(f+4) == 0:
            return False
        f += 6
    return True

def prime_factors(factors):
    tmplst = sorted(factors)
    if len(tmplst) < 1:
        return []
    prime_fact = []
    for elem in tmplst:
        if is_prime(elem):
            prime_fact.append(elem)
    return prime_fact

factors_lst = []
n = 0
while n < 1000000:
    n += 1
    factors_lst = prime_factors(factors(n))
    if len(factors_lst) == 4:
        if len(prime_factors(factors(n+1))) == 4 and len(prime_factors(factors(n+2))) == 4 and len(prime_factors(factors(n+3))) == 4:
            break

print n, factors_lst
print n+1, prime_factors(factors(n+1))
print n+2, prime_factors(factors(n+2))
print n+3, prime_factors(factors(n+3))
