def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x

xx=10**9+7
n=int(input())
ls=list(map(int,input().split()))

if len(ls)==1:
    n=ls[0]
    print((n**n)%xx)
else:
    p=1
    for i in ls:
        p*=i

    x,y=ls[0],ls[1]
    g=find_gcd(x,y)
    

    for i in range(2,len(ls)):
        g=find_gcd(g,ls[i])
    print((p**g)%xx)
