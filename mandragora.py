for _ in range(int(input())):
    n=int(input())
    H=[int(x) for x in input().split()]
    ls=sorted(H)
    s,p=n,0
    m,a=0,0
    for i in range(n):
        m=m+ls[n-i-1]
        p=m*s
        if p>a:
            a=p
        s-=1
    print(a)
