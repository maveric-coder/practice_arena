_=int(input())
ls=[int(x) for x in input().split()]
s=0
for i in ls:
    s+=i
if s%2==1:
    print("NO")
else:
    count=0
    for i in range(len(ls)):
        if ls[i]%2!=0:
            ls[i]=ls[i]+1
            ls[i+1]=ls[i+1]+1
            count+=2
    print(count)

