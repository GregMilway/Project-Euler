#600851475143

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i = i+6
    return True

inp = raw_input('enter number: ')
if inp == '':
    num = 600851475143
else:
    num = int(inp)
num_list = list()

target = num
index = 2

while index < target:
    if num%index == 0:
        num_list.append(index)
        num_list.append(num/index)
        target = num/index
    index = index + 1
num_list.sort()
num_list.reverse()

for el in num_list:
    if isPrime(el):
        print el

