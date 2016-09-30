# count the number of times n choose r is > 1,000,000 for  1<= n <= 100.

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
subtot = 0
for n in range(1,101):
    for k in range(1,n+1):
        if choose(n,k) > 1000000:
            subtot += 1

print subtot
