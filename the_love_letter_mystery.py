for _ in range(int(input())):
    st=input()
    al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',    'u','v','w','x','y','z']
    n=int(len(st)/2)

    f=st[:n]
    if len(st)%2==1:
        n+=1
    s=st[n:]
    s=s[::-1]
    su=0
    if f!=s:
        for i in range(len(s)):
            xx=al.index(f[i])-al.index(s[i])
            if xx<0:
                xx*=-1
            su=su+xx
    print(su)
