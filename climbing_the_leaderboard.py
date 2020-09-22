from collections import Counter
m=input()
r=[int(x) for x in input().split()]
n=input()
s=[int(x) for x in input().split()]

ls=list(Counter(r).keys())

st=[]
k=len(ls)-1
for i in s:
    for j in range(k,-1,-1):
        if ls[j]>i:
            st.append(j+2)
            k=j
            break
        elif j==0:
            st.append(1)

for i in st:
    print(i)
