from itertools import combinations 
def val_tr(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return 1
    else:
        return -1

_=input()
ls=[int(x) for x in input().split()]
st=list(combinations(ls,3))
ss=[]
zz=0
for i in range(len(st)):
    m,n,o=st[i][0],st[i][1],st[i][2]
    x=val_tr(m,n,o)
    if x>0 and m+n+o>zz:
        zz=m+n+o
        ss.append(st[i])
if len(ss)==0:
    print(-1)
else:
    print(*(sorted(max(ss))))
