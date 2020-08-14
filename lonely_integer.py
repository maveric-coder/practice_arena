_=input()
ls=[int(x) for x in input().split()]
st=[]
c=[]
for i in ls:
    if i not in st:
        st.append(i)
        c.append(ls.count(i))

print(st[c.index(min(c))])
