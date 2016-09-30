 #count letters used when numbers 1 - 1000 are written as a list of words

numwords = {
 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred',
 1000: 'thousand'
}

wordstring = ''

def num2word(n):
    if n <= 20:
        return numwords[n]
    elif n < 100:
        tens, unit = divmod(n, 10)
        return numwords[tens*10] + numwords[unit]
    elif n < 1000:
        tuns, num = divmod(n, 100)
        if num == 0:
            return numwords[tuns] + numwords[100]
        elif num <= 20:
            return numwords[tuns] + numwords[100] + 'and' + numwords[num]
        else:
            tens, unit = divmod(num, 10)
            return numwords[tuns] + numwords[100] + 'and' + numwords[tens*10] + numwords[unit]
    else:
        return numwords[1] + numwords[1000]

for i in range(1,1001):
    wordstring += num2word(i)

print len(wordstring)
