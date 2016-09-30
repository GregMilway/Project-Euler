inp  = raw_input('enter range: ')
rng = int(inp)

total = 0

for index in range(rng):
    if index%3 == 0 or index%5 == 0:
        total = total + index

print total
