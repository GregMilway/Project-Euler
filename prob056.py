# for the natural numbers, a,b < 100, what is the maximal digit sum of a**b

max_sum = 0

def digitsum(n):
    return sum(map(int,str(n)))

for a in xrange(100):
    for b in xrange(100):
        tmpsum = digitsum(a**b)
        if tmpsum > max_sum:
            max_sum = tmpsum

print max_sum
