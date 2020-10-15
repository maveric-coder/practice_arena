n =int(input())
ls=list(map(int,input().split()))
s=sum(ls)
st=[]
for i in range(n):
    temp=s-ls[i]
    if temp%7==0:
        st.append(ls[i])
if st:
    print(ls.index(min(st)))
else:
    print("-1")
