from math import ceil
m,n=map(int,input().split())
ls=[int(x) for x in input().split()]
sp=0
ch=1
for i in ls:
    for j in range(ceil(i/n)):
            if ch>j*n and ch<=j*n+min(n,i):
                sp+=1
            i-=n
            
            ch+=1
    
print(sp)

