# for all 0-9 pandigital numbers, find those with the following property, for dn is the nth digit:
# d1d2d3%2  == 0
# d2d3d4%3  == 0
# d3d4d5%5  == 0
# d4d5d6%7  == 0
# d5d6d7%11 == 0
# d6d7d8%13 == 0
# d7d8d9%17 == 0

import itertools

def list3_to_num(lst): # turns 3-element list to a number
    return lst[0]*100+lst[1]*10+lst[2]

pan_sum = 0
primes = [2,3,5,7,11,13,17]
# create list of all 0-9 pan-digital numbers, or devise a generator? Generator would be more efficient

#for x in xrange(1023456789,9876543210):
#    if sorted(str(x)) == ['0','1','2','3','4','5','6','7','8','9']:
#        pan_list.append(x)

pan_list = itertools.permutations(range(10))

while True:
    primepan = True
    try:
        num = pan_list.next()
    except:
        break

    for i in range(7):
        if list3_to_num(num[i+1:i+4])%primes[i] != 0:
            primepan = False
            break

    if primepan:
        pan_sum += int(''.join(map(str,num)))

print pan_sum
