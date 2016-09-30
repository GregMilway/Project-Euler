#find product of a and b, where n^2 +a*n +b gives most consecutive primes
#such that |a| and |b| less than 1000.
#


def is_prime(x):
    if x >= 2:
        for y in range(2,int(x**0.5)+1):
            if not ( x % y ):
                return False
    else:
        return False
    return True

maxprimes = 0
primea = 0
primeb = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        primelength = 0
        while True:
            if is_prime(n**2+a*n+b):
                primelength += 1
                n +=1
            else:
                break
        if primelength > maxprimes:
            maxprimes = primelength
            primea = a
            primeb = b

print primea*primeb
