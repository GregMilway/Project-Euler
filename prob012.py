#find first triangle number with over 500 factors
# triangle number n = sum of ints from 1 to n

#triangle num function:

def triangle_num(n):
    return sum(range(1,n+1))

def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

n = 2
triag_num = 0

while len(factors(triag_num)) < 501:
    triag_num = triangle_num(n)
    n += 1

print triag_num
