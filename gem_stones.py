ls=[]
ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for _ in range(int(input())):
    ls.append(input())
st=[]
for i in ll:
    f=1
    for j in ls:
        if i in j:
            f=f and 1
        else:
            f=f and 0
    if f==1:
        st.append(i)
print(len(st))
