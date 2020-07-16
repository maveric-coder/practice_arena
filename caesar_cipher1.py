_=input()
st=input()
n=int(input())
if n>26:
    n=n%26
ol="abcdefghijklmnopqrstuvwxyz"
al=ol[n:]+ol[:n]
st1=""
for i in st:
    if i.isalpha():
        ind=0
        xx=i
        xx=i.lower()
        ind=(ol.index(xx))
        if i.isupper():
            yy=al[ind]
            st1=st1+yy.upper()
      
        else:
            st1=st1+al[ind]
        
    else:
        st1=st1+i 
        
print(st1)
