_,m=map(int,input().split())
ls=[int(x) for x in input().split()]
for y in range(m):
    i,j=map(int,input().split())
    st=[]*0
    for xx in range(i,j+1):
        st.append(ls[xx])
    print(min(st))


