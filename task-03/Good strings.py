n=int(input(""))
if n>=1 and n<=100:
    s=input("")
    i=0
    for x in s:
        if x=="1" or x=="0":
            i+=1
    print(i)
