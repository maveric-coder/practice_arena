from math import ceil
s,x,n=map(int,input().split())
d=s

ls=[]
for _ in range(n):
    ls.append(list(map(int,input().split()))) 
ls.sort()

i=0
j=0   
while d>0:
    if j<n:
        if ls[j][0]-1==i:
            d-=ls[j][1]
            i+=1
            j+=1
        else:
            a=ls[j][0]
            b=ls[j-1][0]+1 if j>0 else 1
            zz=(a-b)*x
            if zz<d:
                d-=zz
                i+=zz//x
            else:
                j=n 
    else:
        i+=ceil(d/x)
        d-=x*ceil(d/x)
print(i)
