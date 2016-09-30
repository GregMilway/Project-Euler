# find number of paths in 20x20 grid, going right and down.
#calculate central binomial coefficient

import math

top = math.factorial(40)

bot = (math.factorial(20))**2

print top/bot
