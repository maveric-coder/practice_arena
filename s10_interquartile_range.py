import statistics as st

n=int(input())
ss=[int(x) for x in input().split()]
f=[int(x) for x in input().split()]
ls=[]
for i in range(n):
    ls+=[ss[i]]*f[i]
ls=sorted(ls)

N=sum(f)
if N%2==1:
    q1=st.median(ls[:N//2])
    q3 = st.median(ls[N//2+1:])
else:
    q1 = st.median(ls[:N//2])
    q3 = st.median(ls[N//2:])
print(round(1.0*(q3-q1),1))
