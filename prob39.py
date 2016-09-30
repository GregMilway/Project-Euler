#find the perimeter, p, which gives the most Pythagorean triples such that a+b+c = p
# such that p <= 1000


triag_count = 0 #for each length of perimeter, we need to count how many right-triangles we can make
max_triag = 0
max_p = 0 #track the perimeter that gives the most triangles

for p in range(3,1001):     #smallest perimeter of an integer triangle is 3
    triag_count = 0
    for a in range(1,p//3):
        bctot = p - a
        b = a + 1
        c = bctot - b
        while b < c:
            if a**2 + b**2 == c**2:
                triag_count += 1
            b +=1
            c -=1
        if triag_count > max_triag:
            max_triag = triag_count
            max_p = p

print max_p
