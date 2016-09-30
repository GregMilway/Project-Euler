#how many Lychrell numbers below 10,000?
# given the process of reversing the digits of a number, and adding it to itself:
# 47 +74 = 121, if a given number does not produce a palindrome number, then it is Lychrell.
# for the purpose of this program, if it does not produce a palindrome in 50 iterations, it is a Lychrell number.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

subtot = 0
for i in xrange(10000):
    num = i
    for x in xrange(50):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            break
    else:
        subtot += 1

print subtot
