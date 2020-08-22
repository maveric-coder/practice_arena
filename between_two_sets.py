n,m=map(int,input().split())
ls1=[int(x) for x in input().split()]
ls2=[int(x) for x in input().split()]
mi=min(ls2)
st=[]
x=1
ff=max(ls1)
i=1
while x>0:
    if ff*i<=mi:
        
        st.append(ff*i)
        i+=1
    else:
        x=0
count=0
for i in st:
    f1,f2=1,1
    for k in range(len(ls1)):
        if i%ls1[k]!=0:
            f1=0
    for k in range(len(ls2)):
        if ls2[k]%i!=0:
            f2=0
    if f1==1 and f2==1:
        count+=1
print(count)
