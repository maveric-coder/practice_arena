m,n=map(int,input().split())
ls=[int(x) for x in input().split()]
st=[ls[0]]
for i in range(1,len(ls)):
    st.append(ls[i]+st[i-1])
for _ in range(n):
    ans=0
    l,r=map(int,input().split())
    if l==1:
        ans=st[r-1]//(r-l+1)
    else:
        ans=(st[r-1]-st[l-2])//(r-l+1)
    print(ans)
