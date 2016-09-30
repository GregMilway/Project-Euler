# find sum of amicable numbers below 10000.
#example:
# 220 = 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, the sum of which is 284
# 284 = 1, 2, 4, 71, 142 which sums to 220
# thus, 220 and 284 are an amicable pair

#find factors of a number

def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

#find potential amicable partner of a number
def find_amic(num):
    subtot = factors(num)
    subtot.discard(num)
    return sum(subtot)

#check if actually is an amicable number
def is_amic(num):
    return find_amic(num) != num and num == find_amic(find_amic(num))


amicable = set()

for i in range(10000):
    if is_amic(i):
        amicable.add(i)

print sum(amicable)
