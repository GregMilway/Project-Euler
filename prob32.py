#pan-digital numbers:
# an n-digit number is pan-digital if it has all digits 1-n, eg: 12345.
#special case, where two ints and their product is pan-digital, eg:
#39*186 = 7254

def is_anagram(a,b):
    if len(a) != len(b):
        return False
    else:
        return sorted(a) == sorted(b)

def is_pandigital(x,y):
    tmp = str(x)+str(y)+str(x*y)
    return is_anagram(tmp,'123456789')

pandigits = []

for i in range(2,100):
    if i > 9:
        k = 123
    else:
        k = 1234
    end = 10000/ i + 1
    for j in range(k,end):
        if is_pandigital(i,j):
            pandigits.append(i*j)

print sum(set(pandigits))
