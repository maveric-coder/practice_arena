n=int(input())
ls=[int(x) for x in input().split()]
ls=sorted(ls)
zz=1

while zz>0 and ls[-1]>0:
    m=0
    f=1
    i=0
    count=0
    while f>0 and i<len(ls):
        if ls[i]>0:
            m=ls[i]
            f=0
        else:
            i+=1
    for i in range(len(ls)):
        if ls[i]>=m:
            count+=1
            ls[i]=ls[i]-m
    print(count)

