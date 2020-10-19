def shifter(ls,n,d):

    st=[]
    
    if d=='L':
        st=ls[n:]+ls[:n]
        
    else:
        st=ls[-n:]+ls[:-n]
    
    return st
for _ in range(int(input())):
    s,n,d=map(str,input().split())
    n=int(n)
    ls=[]

    s=bin(int(s))
    
    ls[:]=s[2:]
    xx=len(ls)
    ls=['0']*(16-xx)+ls

    
    ls=shifter(ls,n,d)
    
    st=(''.join(ls))
    print(int(st,2))
