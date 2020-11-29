a=int(input(""))
for y in range(0,a):
    k=int(input(""))
    b=input("")
    l=[]
    a=""
    c=[]
    p=0
    i=1
    for x in b:
        h=len(b)
        if x==" " or i==h:
            a=a+x
            p=p+ord(x)
            l.append(a)
            a=""
            c.append(p)
            p=0
        else:
            a=a+x
            p=p+ord(x)
        i+=1
    if len(l)>k:
        y=c[k]
        print(y)
    else:
        print("-1")
