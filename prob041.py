import primesieve as ps

def is_anagram(a,b):
    if len(a) != len(b):
        return False
    else:
        return sorted(a) == sorted(b)

def digits(n):
    return map(int, str(n))

def is_pan_n(num):
    return is_anagram(str(num),'1234567')

primelst = ps.generate_primes(1000000,10000000)
max_pan_prime = 0

for prime in reversed(primelst):
    if is_pan_n(prime):
        max_pan_prime = prime
        break

print max_pan_prime
