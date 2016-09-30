#find the sum of the diagonals on a clockwise spiral in a grid of 1001x1001

#first, create empty list to hold elements:

subtot = 1
tot = 1
for i in range(2,1001,2):
    for j in range(4):
        subtot += i
        tot += subtot

print tot
