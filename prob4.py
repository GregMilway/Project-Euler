num_list = list()
for iii in range(100,1000):
    for jjj in range(100,1000):
        num_list.append(iii*jjj)
num_list.sort()

for el in num_list:
    if (str(el) == str(el)[::-1]):
        print el
