# find four adjacent numbers in grid with maximum product
# up, down, left right, or diagonal.
# due to commutation, up = down, left = right, nw-se = se-nw, and sw-ne = ne-sw
# thus, only four directions are needed to be checked; for simplicity, use
# down, right, nw-se, and ne-sw.

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p
#import array:
numgrid = []

with open('prob11grid') as f_num:
    for i in range(20):
        numgrid.append([int(num) for num in f_num.readline().split()])

rghtlst = []
downlst = []
nwselst = []
neswlst = []

#check right
for i in range(20):
    for j in range(17):
        tmplst = numgrid[i][j:j+4]
        if 0 not in tmplst and sum(tmplst) > sum(rghtlst):
            rghtlst = tmplst
#check down
for i in range(17):
    for j in range(20):
        tmplst = []
        for k in range(4):
            tmplst.append(numgrid[i+k][j])
        if 0 not in tmplst and sum(tmplst) > sum(downlst):
            downlst = tmplst

#check north west - south east

for i in range(17):
    for j in range(17):
        tmplst = []
        tmplst2 = []
        for k in range(4):
            tmplst.append(numgrid[i+k][j+k])
            tmplst2.append(numgrid[i+k][19 - (j+k)])
        if 0 not in tmplst and sum(tmplst) > sum(nwselst):
            nwselst = tmplst
        if 0 not in tmplst2 and sum(tmplst2) > sum(neswlst):
            neswlst = tmplst2

print product(rghtlst)
print product(downlst)
print product(nwselst)
print product(neswlst)
