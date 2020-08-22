_,d=map(int,input().split())
ls=[int(x) for x in input().split()]
count=0
for i in range(len(ls)):
    if ls[i]+d in ls and (ls[i]+(2*d)) in ls:
        count+=1
print(count)

