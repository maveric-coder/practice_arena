from collections import Counter
ls=Counter()
for _ in range(int(input())):
    m,n=map(int,input().split())
    if m==1:
        if n in ls:
            ls[n]+=1
        else:
            ls.update({n:1})
    elif m==2:
        if n in ls and ls[n]>0:
            ls[n]-=1
    elif m==3:
        zz=list(ls.values())
        
        if n in zz:
            print(1)
        else:
            print(0)
