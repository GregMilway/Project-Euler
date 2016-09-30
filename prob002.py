count1 = 1
count2 = 1
count = 1
total = 0

while count < 4000000:
    if count%2 == 0:
        total = total + count
    count = count1 + count2
    count1 = count2
    count2 = count

print total
