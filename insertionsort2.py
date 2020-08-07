n=input()
a=[int(x) for x in input().split()]
for i in range(1,len(a)):
    j=a.index(a[i])
    while j>0:
        if a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
            
        j-=1
    print(*a)
