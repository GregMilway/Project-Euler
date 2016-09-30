 # find two pentagonal numbers (p(n) = n(3n-1)/2,), p(j) and p(k), such that p(j)+p(k) and p(j)-p(k) are both pentagonal,

def is_pent(n):
    if n <= 0:
        return False
    tmp = ((24.0*n+1.0)**0.5+1.0)/6.0
    return tmp == int(tmp)

def pent(n):
    return n*(3*n-1)/2

found = False
i = 1
while not found:
    i+= 1
    n = pent(i)
    for j in reversed(range(1,i)):
        m = pent(j)
        if is_pent(n+m) and is_pent(abs(n-m)):
            print n, m
            print abs(n-m)
            found = True
            break
