# find an integer, x, such that 2*x, 3*x, 4*x, 5*x and 6*x are permutations of x

def is_permutation(a,b):
    return sorted(str(a)) == sorted(str(b))

x = 0
found = False
while not found:
    x += 1
    for i in range(2,7):
        if not is_permutation(x,i*x):
            break
    else:
        found = True

print x
