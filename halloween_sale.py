s,d,m,amt=map(int,input().split())
count=0
if amt>s:
    tot=s
    count=1
    while tot<amt:
        if s-d>m:
            s=s-d
            tot=tot+s
            
        else:
            tot=tot+m
        if tot<=amt:
            count+=1

else:
    count=0

print(count)
    
