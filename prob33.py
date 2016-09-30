#find all non-trivial incorrectly cancelled fractions, e.g. 49/98 = 4/8 by cancelling the 9's

def shared_digit(a,b):
    lefta = a//10
    righta = a%10
    leftb = b//10
    rightb = b%10
    if lefta == rightb:
        return lefta
    elif righta == leftb:
        return righta
    else:
        return None

nums = range(1,10)

twodigit = []
fractions = []
anom_fractions = []


for i in nums:
    nums2 = [x for x in nums if x != i]
    for j in nums2:
        twodigit.append(i*10+j)

fractions = [(twodigit[i],j) for i in range(len(twodigit)-1) for j in twodigit[i+1:] if shared_digit(twodigit[i],j) is not None]

for tup in fractions:
    shared = shared_digit(tup[0],tup[1])
    anom_n = int(str(tup[0]).replace(str(shared),''))
    anom_d = int(str(tup[1]).replace(str(shared),''))
    if float(tup[0]) / float(tup[1]) == float(anom_n) / float(anom_d):
        anom_fractions.append(tup)

print anom_fractions
