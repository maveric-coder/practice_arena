st=input()
st=st.lower()
ls=['a','b','c','e','f','g','h','i','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
c=1
for i in ls:
    if i in st:
        c=c and 1
    else:
        c=c and 0
if c==1:
    print("pangram")
else:
    print("not pangram")
