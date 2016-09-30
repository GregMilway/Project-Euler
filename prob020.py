# sum of digits of 100!

import math

num = math.factorial(100)
#num = int(raw_input('enter a number: '))
subtot = 0

while num > 0 :
     num, rem = divmod(num, 10)
     subtot += rem

print subtot
