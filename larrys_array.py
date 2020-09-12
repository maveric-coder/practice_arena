def larrysArray(a):
    c=0
    for i in range(1,len(a)):
        j=a.index(a[i])
        while j>0:
            if a[j-1]>a[j]:
                a[j],a[j-1]=a[j-1],a[j]
                c+=1
            j-=1
    if c%2==0:
        return "YES"
    else:
        return "NO"
