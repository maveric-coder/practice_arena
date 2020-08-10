for _ in range(int(input())):
    st=input()
    ls=[]
    sc=[]
    lr=[]
    rc=[]
    sr=st[::-1]
    for i in st:
        ls.append(ord(i))
    for i in sr:
        lr.append(ord(i))
    f=1
    for i in range(len(ls)-1):
        xx=ls[i]-ls[i+1]
        if xx<0:
            xx=xx*-1
        sc.append(xx)
    
        xx=lr[i]-lr[i+1]
        if xx<0:
            xx=xx*-1
        rc.append(xx)
    if sc==rc:
        print("Funny")
    else:
        print("Not Funny")
