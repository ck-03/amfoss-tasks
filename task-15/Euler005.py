def gcd(x,y):
    return y and gcd(y, x % y) or x
def lcm(x,y):
    return x * y / gcd(x,y)
t=int(input(""))
if t>=1 and t<=10:
    for q in range(t):
        n =int(input(""))
        if n>=1 and n<=40:
            for i in range(1, n+1):
                n = lcm(n, i)
        print(int(n))

                
