#find d such that 1/d has longest reciprocal cycle, with d < 1000

def divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while True:  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)
divtup = (0,[],[])
track = 0
for i in range(1,1000):
    tmptup = divide(1,i)
    if len(tmptup[2]) > len(divtup[2]):
        divtup = tmptup
        track = i
print track
