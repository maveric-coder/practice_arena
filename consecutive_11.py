m,n=map(int,input().split())
ls=list(map(int,input().split()))
ls.insert(0,0)
c=0
for i in range(1,m+1):
    if '11' in bin(ls[i]):
        c+=1
    ls[i]=c 
for _ in range(n):
    a,b=map(int,input().split())
    print(ls[b]-ls[a-1])
