for _ in range(int(input())):
    st=input()
    j=1
    m=0
    f=1
    while j<=len(st)/2 and f>0:
        ls=int(st[:j])
        m=ls
        ss=""
        while len(ss)<len(st):
            ss=ss+str(ls)
            ls+=1
        if ss==st:
            f=0
            print("YES "+str(m))
        else:
            j+=1
    if f==1:
        print("NO")
