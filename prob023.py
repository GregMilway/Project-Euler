# find sum of all integers that cannot be expressed as a sum of two abundant numbers.
# an abundant number is one such that the sum of its proper divisors is greater than itself
# example: 12: 1+2+3+4+6 = 16, which is greater than 12.
# proven that all integers above 28123 can be expressed as sum of two abundant numbers, thus:
# create function that checks for abundance
# create list of natural numbers 1 - 28123
# create list of abundant numbers up to 28123
# sum each pair of abundant numbers from list, and if result is in natural numbers list, remove it.
# use sets?

def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def is_abundant(n):
    fact = factors(n)
    fact.discard(n)
    return sum(fact) > n

natural_numbers = set(range(1,28124))

abundant_numbers = []

for i in range(1,28124):
    if is_abundant(i):
        abundant_numbers.append(i)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        num = abundant_numbers[i] + abundant_numbers[j]
        if num in natural_numbers:
            natural_numbers.discard(num)

print sum(natural_numbers)
