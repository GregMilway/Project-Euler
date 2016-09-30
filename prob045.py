# given that the triangle number T285 is also pentagonal and hexagonal, find the next triangular number that is the same.

def triag(n):
    return n*(n+1)/2

def is_pent(n):
    if n <= 0:
        return False
    tmp = ((24.0*n+1.0)**0.5+1.0)/6.0
    return tmp == int(tmp)

def is_hexag(n):
    if n <= 0:
        return False
    tmp = ((8.0*n+1.0)**0.5+1.0)/4.0
    return tmp == int(tmp)

n = 285

while True:
    n += 1
    num = triag(n)
    if is_pent(num) and is_hexag(num):
        print num
        break
