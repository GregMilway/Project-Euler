# find starting number with longest Collatz sequence, below 1million

# next number in collatz sequence is: n/2 (if n is even), or 3n+1 (if n is odd)


def next_collatz(n):
    if not n%2:
        return n/2
    else:
        return 3*n + 1



collatz_list = []
bignum = 0

for i in range(1,1000000):
    num = i
    tmp_list = []
    while True:
        tmp_list.append(num)
        if num == 1: break
        num = next_collatz(num)
    if len(tmp_list) > len(collatz_list):
        collatz_list = tmp_list
        bignum = i

print bignum
