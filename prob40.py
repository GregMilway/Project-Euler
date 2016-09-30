# find the 1st, 10th, 100th, 1000th, 10000th, 100000th and 1000000th digit of the fractional part of Champernowne's constant.
# brute force solution:

n = 1

champstr = ''

while len(champstr) < 1000000:
    champstr+=str(n)
    n += 1

idx = [0,9,99,999,9999,99999,999999]

prod = 1
for i in idx:
    prod *= int(champstr[i])

print prod
