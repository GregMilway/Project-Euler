# find all integers below 1000000 that are palindromes in base 10 and base 2


dbl_palindromes = []

for i in xrange(1,1000000):
    base10str = str(i)
    base2str = '{0:b}'.format(i)
    if base10str == base10str[::-1] and base2str == base2str[::-1]:
        dbl_palindromes.append(i)

print sum(dbl_palindromes)
