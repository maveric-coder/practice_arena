st=input()
ls=[]
c=[]
for i in st:
    if i not in ls:
        ls.append(i)
        c.append(st.count(i))

count=0
for i in c:
    if i%2==1:
        count+=1
if len(st)%2==0 and count==0:
    print("YES")
else:
    if len(st)%2!=0 and count==1:
        print("YES")
    else:
        print("NO")
