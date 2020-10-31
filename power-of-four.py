from itertools import combinations
ls=[]
for i in range(10):
    ls.append(4**i)

st=[]
for i in range(1,len(ls)+1):
    xx=list(combinations(ls,i))
    for j in xx:
        st.append(sum(j))
st.sort()
for _ in range(int(input())):
    n=int(input())
    if n in st:
        print(n)
    else:
        i=0
        while st[i]<=n:
            i+=1
        print(st[i])
