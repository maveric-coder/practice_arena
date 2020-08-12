n=int(input())
ls=[int(x) for x in input().split()]
ls=sorted(ls)
if n%2==1:
    print(ls[(len(ls)//2)])
else:
    x=len(ls)/2
    print(((ls[x-1]+ls[x])/2))
