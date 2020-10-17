from collections import Counter
n=input()
ls=list(map(int,input().split()))

ls.sort()

st=list(Counter(ls).values())
st1=list(Counter(ls).keys())
n=len(st1)
ss=[]
i=0


while i<n:
    if st[i]==1:
        ss.append(st1[i])
    i+=1
print(*ss)
