_=input()
ls=[int(x) for x in input().split()]
ll=[]
lr=[]
lq=[]
p=ls[0]
j=0
while j<len(ls):
    if ls[j]>p:
        lr.append(ls[j])
    elif ls[j]<p:
        ll.append(ls[j])
    else:
        lq.append(ls[j])
    j+=1

print(" ".join(str(i) for i in (ll+ lq+lr)))
