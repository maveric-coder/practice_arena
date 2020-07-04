p=int(input())
q=int(input())
ls=[]
for i  in range(p,q+1):
    n=i**2
    d=len(str(i))
    x=str(n)
    r=int(x[-d:])
    if len(x)<2:
        l=0
    else:
        l=int(x[:-d])
    if l+r==i:
        ls.append(i)

if ls:
    print(*ls)
else:
    print("INVALID RANGE")
