# pan-digital multiples
# largest 9-digit pan-digital number
#that can be created by concatenating the products of some integer k and a list of integers [1,2,...,n] for n > 1

def is_anagram(a,b):
    if len(a) != len(b):
        return False
    else:
        return sorted(a) == sorted(b)

for i in range(9487,9233,-1):
    if is_anagram((str(i)+str(i*2)),'123456789'):
        print (str(i)+str(i*2))
        break
