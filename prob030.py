#find the sum of all numbers that can be written as the sum of the fifth powers of their digits
#example ABCDE = A**5 + B**5 + C**5 + D**5 + E**5

def is_five_narc(n):
    subtot = 0
    for digit in  str(n):
        subtot += int(digit)**5
    return n == subtot

five_narc_list = []

for i in range(2,355000):
    if is_five_narc(i):
        five_narc_list.append(i)

print sum(five_narc_list)
