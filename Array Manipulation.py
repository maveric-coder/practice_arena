from collections import Counter
m,n=map(int,input().split())
#c=[0]*m
c=Counter()
for _ in range(n):
    a,b,z=map(int,input().split())
    c[a]+=z
    c[b+1]-=z
mS=0
zS=0

for i in sorted(c)[:-1]:
    mS+=c[i]
    zS=max(zS,mS)
    
    
print(zS)
