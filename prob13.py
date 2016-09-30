# compute first 10 digits of sum of 100 50-digit numbers.

#first attempt: simply sum the numbers (will probably fail)

#HAH! WOrked fine :)
numlst = []

with open('prob13nums') as f_num:
     for i in range(100):
         numlst.append(int(f_num.readline().strip()))
print sum(numlst)
