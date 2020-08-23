st=[]
q=[]
for _ in range(int(input())):
    st.append(input())
for _ in range(int(input())):
    q.append(input()) 
ls=[]
for i in q:
    ls.append(st.count(i))
[print (i) for i in ls]
    

