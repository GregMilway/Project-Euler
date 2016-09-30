subtotal = 0
subtotal_squares = 0

for i in range(1,101):
    subtotal = subtotal + i
    subtotal_squares = subtotal_squares + i**2
print subtotal**2 - subtotal_squares
