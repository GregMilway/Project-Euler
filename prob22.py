#find total name score for list of names in prob22.txt
#1) sort list of names alphabetically
#2) calculate alphabetical score of each name (a = 1, b = 2, etc)
#3) multiply score with position for each name, and find total score for the list.


with open('prob22.txt') as f_names:
    names = f_names.read().split('","')

names[0] = names[0].lstrip('"')
names[-1] = names[-1].rstrip('"')

names.sort()

letter_scores = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

subtot = 0
for i in range(len(names)):
    namescore = 0
    for j in names[i]:
        namescore += letter_scores[j]
    subtot += namescore * (i + 1)

print subtot
