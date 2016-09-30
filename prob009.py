# Pythagorean triplet: a**2 + b**2 == c**2
# with constraints a < b < c and a + b + c == 1000
# find product a * b * c

# calculate all possible combinations for a,b,c satisfying constraints

# start with a = 1, b = 2, c = 997 (test for b+c == 999), while b < c.
# maximum value for a is 332,
tuplst = []
for a in range(1,333):
    bctot = 1000 - a
    b = a + 1
    c = bctot - b
    while b < c:
        tuplst.append((a,b,c))
        b += 1
        c -= 1

for tup in tuplst:
    if tup[0]**2 + tup[1]**2 == tup[2]**2:
        break

print tup[0]*tup[1]*tup[2]
