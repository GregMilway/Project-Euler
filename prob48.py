# find the last 10 digits of the series 1**1+2**2+3**3...1000**1000

subtot = 0

for i in xrange(1000):
    subtot += (i+1)**(i+1)

print subtot%10000000000
