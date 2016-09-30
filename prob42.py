# for each word in prob42words, calculate word score (as prob22)
# check word score is triangular number, if so, increment the count.

def is_triag(n):
    k = int((2*n)**0.5)
    return n == (k*(k+1)/2)

def word_score(word):
    sum = 0
    for letter in word:
        sum += letter_scores[letter]
    return sum

with open('prob42words') as f_words:
    words = f_words.read().split('","')

words[0] = words[0].lstrip('"')
words[-1] = words[-1].rstrip('"')

letter_scores = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

triag_words = 0

for word in words:
    if is_triag(word_score(word)):
        triag_words += 1

print triag_words
