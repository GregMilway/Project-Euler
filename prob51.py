# By replacing the first digit in the two digit number: *3, we generate 6 primes out of 9 numbers:
# 13, 23, 43, 53, 73, 83
# By replacing the third and fourth digits in the five digit number: 56**3, we get seven primes:
# 56003, 56113, 56333, 56443, 56663, 56773, 56993
# By replacing some digits of some n-digit number (which may not be adjacent), find the smallest prime
# of an 8-prime chain.

import primesieve as ps

primeIter = ps.Iterator()

def is_prime(n):
    primeIter.skipto(n-1)
    return primeIter.next_prime() == n

def digits(n):
    return map(int, str(n))

def fill_digits(num,fill):
    return [elem if elem else fill for elem in num]

def list_to_num(alist,fill):
    return int(''.join(map(str,fill_digits(alist,fill))))


patterns_2 = [  [1,0,0,0,1],
                [0,1,0,0,1],
                [0,0,1,0,1],
                [0,0,0,1,1]]

patterns_3 = [  [1,1,0,0,0,1],
                [1,0,1,0,0,1],
                [1,0,0,1,0,1],
                [1,0,0,0,1,1],
                [0,1,1,0,0,1],
                [0,1,0,1,0,1],
                [0,1,0,0,1,1],
                [0,0,1,1,0,1],
                [0,0,1,0,1,1],
                [0,0,0,1,1,1]]


primes_2 = range(10,100)
primes_3 = range(100,1000)


prime_cands_2 = []
prime_cands_3 = []

for prime in primes_2:
    for mask in xrange(len(patterns_2)):
        prime_digs = digits(prime)
        prime_cands_2.append([prime_digs.pop(0) if elem else 0 for elem in patterns_2[mask]])

for prime in primes_3:
    for mask in xrange(len(patterns_3)):
        prime_digs = digits(prime)
        prime_cands_2.append([prime_digs.pop(0) if elem else 0 for elem in patterns_3[mask]])


prime_cands = list(set(map(tuple, prime_cands_2 + prime_cands_3)))

prime_cands.sort()
cands_curr = []

for prime in prime_cands:
    start = 0
    cands_curr = []
    if prime[0] == 0:
        start = 1
    cands_curr = [list_to_num(prime,i) for i in range(start,10) if is_prime(list_to_num(prime,i))]
    if len(cands_curr) > 7:
        break
else:
    print "we didn't find any"

print cands_curr
