n,k=map(int,input().split())
ls=[int(x) for x in input().split()]
en=100
t=1
c=0
if n%k==0:
    for i in range(0,n,k):
        if ls[i]==1:
            c=c+3
        else:
         c+=1

else:
    temp=0
    i=0
    while t==1:
        i=i+k
        if i<n and ls[i]==1:
            c=c+3
        else:
            c+=1
        if i>=n-1-(n%k):
            i=k-1-(n%k)
        
print(en-c)
    
    


