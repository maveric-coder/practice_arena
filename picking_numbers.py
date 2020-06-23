from collections import Counter
zz=int(input())
n=list(map(int, input().split()))
n=sorted(n)
c=Counter(n)
c=str(c)
st=[]
a=9
i=9
while c[i]!=',':
    st.append(c[i])
    i+=1
count=int(st[3])
count1=count
count2=count
ind=(n.index(int(st[0])))
for i in (n):
    if i-n[ind]==1:
        count1+=1
for i in (n):
    if i-n[ind]==-1:
        count2+=1
print(count1 if count1>count2 else count2)
