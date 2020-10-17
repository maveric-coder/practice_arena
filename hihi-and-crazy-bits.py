for _ in range(int(input())):
    n=bin(int(input()))
    ls=[]
    ls[:]=n 
    ls=ls[2:]
    n=len(ls)-1
    c=0
    while c<1:
        if ls[n]=='0':
            ls[n]='1'
            c+=1
        n-=1
    
    st= ''.join(ls)
    print(int(st,2))
