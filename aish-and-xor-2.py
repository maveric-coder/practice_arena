n=int(input())
ls=list(map(int,input().split()))

se=[0]*n
us=[0]*n
u=0
s=0

for i in range(len(ls)):
    
    if ls[i]%2:
        s+=1
    else:
        u+=1
    se[i]=s
    us[i]=u

for _ in range(int(input())):
    l,r=map(int,input().split())
    if l>1:
        s=se[r-1]-se[l-2]
        u=us[r-1]-us[l-2]
    else:
        s=se[r-1]
        u=us[r-1]
    if s%2:
        print(1^0,u)
    else:
        print(0,u)
    
    
