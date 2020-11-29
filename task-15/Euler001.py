q=int(input("No of iteration:"))
for w in range(q):
    a=0
    t = int(input("enter a number;"))
    for x in range(1,t):
        if x%3==0 or x%5==0:
            a+=x
    print(a)
