def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
ls=[]

for _ in range(int(input())):
    ls.append(int(input()))

dif=[]
for i in range(1,len(ls)):
    dif.append(abs(ls[i]-ls[i-1]))

g=dif[0]
for i in range(1,len(dif)):
    g=gcd(g,dif[i])
st=[]
i=2
while i*i<=g:
    if g%i==0:
        st.append(i)
        if g//i!=i:
            st.append(g//i)
    i+=1
st.append(g)
st.sort()
print(*st)
