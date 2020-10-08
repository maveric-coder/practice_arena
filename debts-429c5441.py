n,m=map(int,input().split())
ls=[0]*n
for  _ in range(m):
    a,b,c=map(int,input().split())
    ls[a-1]-=c  
    ls[b-1]+=c  
s=0
for i in ls:
    if i>0:
        s+=i    
print(s)
