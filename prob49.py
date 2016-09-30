# find the three 4-digit primes a, b= a+3330, c= a+6660, such that a, b, and c are permutations.
#print the 12 digit number made by concatenating a, b, and c

#for sequence to be valid, c <= 9999, thus a must be at most c - 6660 = 3339.


from primesieve import generate_primes

primes = generate_primes(1000,10000)

def is_permutation(a,b):
    return sorted(map(int, str(a))) == sorted(map(int, str(b)))

for prime in primes:
    if prime+3330 in primes and prime+6660 in primes:
        if is_permutation(prime,prime+3330) and is_permutation(prime,prime+6660):
            print str(prime)+str(prime+3330)+str(prime+6660)
