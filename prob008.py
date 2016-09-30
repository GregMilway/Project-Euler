def product(list):
    p = 1
    for i in list:
        p *= i
    return p


with open('prob8num','r') as numfile:
    numlist = [line.strip() for line in numfile]

numstr = ''.join(numlist)

listnum = map(int, numstr)
print listnum

tmpprd = 0

for i in range(13,1000):
    prdtmp = product(listnum[i-13:i])
    if prdtmp > tmpprd:
        tmpprd = prdtmp
print tmpprd
