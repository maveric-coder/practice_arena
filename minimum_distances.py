n=int(input())
ls=[int(x) for x in input().split()]
count=[]
uq=[]
ind=[]
for i in ls:
    if i not in uq and ls.count(i)>1:
        uq.append(i)
        count.append(ls.count(i))

else:
    for i in uq:
        m=ls.index(i)
        n=0
        res=0
        for j in range(m+1,len(ls)):
            if ls[j]==i:
                n=j
        res=m-n
        if res<0:
            res=res*-1
        ind.append(res)
if not  uq:
    print("-1")
else:
    print(min(ind))

    
