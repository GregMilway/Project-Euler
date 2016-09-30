
#num = int(raw_input('enter number: '))
num = 10
allFactors = False

while not allFactors:
    print num
    allFactors = True

    for i in range(1,11):
        if num%i:
            allFactors = False
    num = num+10
print num

#232792560
