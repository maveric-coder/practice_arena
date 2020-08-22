n,d =map(int,input().split())
ls=[int(x) for x in input().split()]
d=d%n
for i in (ls[d:] + ls[0:d]):
    print(i,end=" ")
