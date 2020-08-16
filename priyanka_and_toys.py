n=int(input())
ls=[int(x) for x in input().split()]
ls=sorted(ls)
x=ls[0]
count=1
i=1
while i<n:
    if ls[i]<=x+4:
        i+=1

    else:
        x=ls[i]
        count+=1
print(count)
