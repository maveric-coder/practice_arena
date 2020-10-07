for _ in range(int(input())):
    a=input()
    b=input()
    c=0
    m=len(a)
    n=len(b)
    sa=set(a)
    sb=set(b)
    if len(sa)<len(sb):
        for i in sa:
            if i in sb:
                x=min(a.count(i),b.count(i))
                m-=x
                n-=x
    else:
        for i in sb:
            if i in sa:
                x=min(a.count(i),b.count(i))
                m-=x
                n-=x
    print(m+n)
