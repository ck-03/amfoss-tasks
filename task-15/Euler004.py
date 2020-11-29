def is_pal(c):
    return int(str(c)[::-1]) == c
q=int(input(""))
for t in range(q):
    x=int(input(""))
    maxpal = 0
    for a in range(100, 1000):
        for b in range(a, 1000):
            prod = a * b
            if prod>x:
                break
            if is_pal(prod) and prod > maxpal:
                maxpal = prod
    print(maxpal)
