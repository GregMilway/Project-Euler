# for a convergent of the continued fraction expansion of 2**0.5,  some of the numerators have more digits than the denominator.
# for the first 1000 expansions, how many have this property?

#using the formula for generalised continued fractions:
#A_n = b_n*A_(n-1) + a_n*A_(n-2)
#B_n = b_n*B_(n-1) + a_n*B_(n-2)

#a_n == 1 for all n
#b_n == 2 for all n >= 1, 0 otherwise
#thus the formula simplifies to:
#A_n = 2*A_(n-1) + A_(n-2)
#B_n = 2*B_(n-1) + B_(n-2)

#the first few expansions are:
#1/1, 3/2, 7/5 17/12

#thus   A_0 = 1, A_1 = 3
#       B_0 = 1, B_1 = 2

#therefore, start with pre-defined A0, A1, B0, B1, calculate A2, B2, then shift along, and keep going

def digit_len(n):
    return len(map(int,str(n)))

subtot = 0

A_0 = 1
A_1 = 3
B_0 = 1
B_1 = 2

for x in xrange(2,1000):
    A_2 = 2*A_1 + A_0
    B_2 = 2*B_1 + B_0
    if digit_len(A_2) > digit_len(B_2):
        subtot += 1
    A_1, A_0 = A_2, A_1
    B_1, B_0 = B_2, B_1

print subtot
