import math

def is_prime_number(x):
    if x >= 2:
        for y in range(2,int(x**0.5)+1):
            if not ( x % y ):
                return False
    else:
        return False
    return True

n = int(raw_input('enter a number: '))

num = 0
count = 0

while count < n:
    num = num + 1
    if is_prime_number(num):
        count = count + 1

print num
