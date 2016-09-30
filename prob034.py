# 145 = 1! + 4! + 5!
# find the sum of all numbers that are the factorial of their digits.
# do not include any single digit number, as can't give them as sums.
import math

def digits(n):
    return map(int, str(n))

shriek = [math.factorial(x) for x in xrange(10)]

total = []
subtotlst = []
subtot = 0

num = int(raw_input('Enter a number: '))

for i in xrange(10,num):
    subtotlst = digits(i)
    subtot = 0
    for n in subtotlst:
        subtot += shriek[n]
    if subtot == i:
        total.append(i)

print total
