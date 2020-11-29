q=int(input(""))
for t in range(q):
    a=int(input(""))
    b=1
    c=2
    e=2
    h=0
    for x in range(a-2):
        d=b+c
        if d>=a:
            break
        b=c
        c=d
        if d%2==0:
            e+=d
    print(e)
