# Truncating primes: eg 3797, 379, 37, 3 and 797 97 7.
#find all truncating primes.

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

primes = sieve_for_primes_to(1000000)
trunc_primes = []

for prime in primes:
    if prime < 10:
        continue
    lefttrunc = True
    rghttrunc = True
    primetmp = str(prime)
    #check left truncation
    while len(primetmp) > 1:
        primetmp = primetmp[1:]
        if int(primetmp) not in primes:
            lefttrunc = False
            break
    if lefttrunc:
        primetmp = str(prime)
        while len(primetmp) > 1:
            primetmp = primetmp[:-1]
            if int(primetmp) not in primes:
                rghttrunc = False
                break
    if lefttrunc and rghttrunc:
        trunc_primes.append(prime)

print sum(trunc_primes)
