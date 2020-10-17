for _ in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))[:n]
    x=0
    for i in ls:
        x^=i    
    y,z=0,0
    mm=x
    for i in ls:
        y^=i
        z=y & (y ^ x)
        if z>mm:
            mm=z
    print(mm)
