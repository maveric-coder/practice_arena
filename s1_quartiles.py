def median(ls):
    n=len(ls)
    if n%2==1:
        print(ls[(len(ls)//2)])
    else:
        x=len(ls)//2
        print(((ls[x-1]+ls[x])//2))
def med(ls):
    x=len(ls)
    m,n=0,0
    if x%2==1:
        m=(x//2)-1
        n=(x//2)+1
        return m,n
    else:
        m=(x//2)-1
        n=(x//2)
        return m,n
n=int(input())
ls=[int(x) for x in input().split()]
ls=sorted(ls)

m,n=med(ls)
ls1=ls[:m+1]

median(ls1)
median(ls)
ls2=ls[n:]

median(ls2)

