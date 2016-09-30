# count number of ways to make 2 pounds from any number of coins
#
# coins available are: 100p, 50p, 20p, 10p, 5p, 2p, and 1p (if 200p allowed, and one to total)

# how much (in pence) do we want to add up to?
target = 200
# how many different ways we've counted
count = 0

# value of available coins, in pence (use tuple, immutable, ordered)
coins = (100, 50, 20, 10, 5, 2, 1)


for a in range(target, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            count +=1

print count
