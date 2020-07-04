import math
ls=str(input())
n=math.sqrt(len(ls))
l=int(n)
m=l+1 
st=""
if l**2==len(ls):
    m=l
    xy=l
else:
    xy=m
for i in range(xy):
        zz=i
        while zz<len(ls):
            
            if zz<(len(ls)):
                st=st+ls[zz]
            zz=zz+m
        st=st+' '
print(st)
