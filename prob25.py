# find first Fibonacci number with 1000 digits.


fib_list = [1,1]
index = 2
while len(str(fib_list[-1])) < 1000:
    tmp = sum(fib_list)
    fib_list[0] = fib_list[1]
    fib_list[1] = tmp
    index += 1

print index
