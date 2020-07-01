ls=str(input())
n=int(input())
ct=0
count=0 
if len(ls)==1 and ls[0]=='a':
    count=n

else:
    ct=ls.count('a')*(n//len(ls))
    m=n%len(ls)
    st=ls[:m]
    count=ct+st.count('a')
    

print(count)
    
