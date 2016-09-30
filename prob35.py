#circular primes
#example: 197. shift the digits, and you get 971 and 719 which are also primes.
#find number of circular primes below 1000000

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

def primecirc(primestr):
    return primestr[1:]+primestr[0]

primes = sieve_for_primes_to(1000000)

circ_primes = []
circprime = True

for prime in primes:
    if prime < 10:
        circ_primes.append(prime)
    else:
        circprime = True
        primestr = str(prime)
        for i in range(len(primestr)-1):
            primestr = primecirc(primestr)
            if int(primestr) not in primes:
                circprime = False
                break
        if circprime:
            circ_primes.append(prime)
print len(circ_primes)
