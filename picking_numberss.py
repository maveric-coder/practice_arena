n=int(input())
ls=[int(x) for x in input().split()]
ls=sorted(ls)
uq=[]
count=[]
tr=[]
for i in ls:
    if i not in uq:
        uq.append(i)
        count.append(ls.count(i))
#print(uq)
if len(uq)==1:
    print (n)
else:
    for i in range(len(uq)-1):
        if (uq[i+1]-uq[i])<=1:
            tr.append(count[i+1]+count[i])
    print(max(tr) if max(tr)>max(count) else max(count))
