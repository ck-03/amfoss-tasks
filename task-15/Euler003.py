q=int(input(""))
for t in range(q):
    a=int(input(""))
    p=1
    for x in range(1,a):
        if a%x==0:
            p=x
    if p==1:
        p=a
    print(p)
