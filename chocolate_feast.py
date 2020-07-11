x=int(input())
for _ in range(x):
    n,c,m=map(int,input().split())
    count=0
    count=count+(n//c)
    wr=0
    wr=n//c 
    f=1
    while f>0:
        ch=wr//m
        count=count+ ch
        wr=(wr%m)+ch
        if wr<m:
            f=0
    print(count)

