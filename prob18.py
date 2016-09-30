# traverse triangle of numbers, find largest path
#try greedy algorithm (take biggest chunk I can now,)

numlst = []
subtot = []
with open('prob18triag') as f_nums:
    for i in range(15):
        numlst.append([int(x) for x in f_nums.readline().split()])

while len(numlst) > 1: #we need to pop two lists from numlst each time
    #pop the last two lists from numlst
    tmplst1 = numlst.pop()
    tmplst2 = numlst.pop()
    #for each value in tmplst2, find the best choice from tmplst1, and add it to item in tmplst2
    for i in range(len(tmplst2)):
        if tmplst1[i] > tmplst1[i+1]:
            tmplst2[i] += tmplst1[i]
        else:
            tmplst2[i] += tmplst1[i+1]
    #add the new list back on the end of numlst
    numlst.append(tmplst2)
    #rinse and repeat

print numlst
