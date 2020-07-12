n=int(input())
for _ in range(n):
    st=str(input())
    ls=[]
    for i in st:
        ls.append((i))
    i=len(ls)-1
    while i>0 and ls[i-1]>=ls[i]:
        i-=1
        
    if i<=0:
        print("no answer")
    else:
        j=len(ls)-1
        while ls[j]<=ls[i-1]:   
            j-=1
        ls[i - 1], ls[j] = ls[j], ls[i - 1]

        ls[i : ] = ls[len(ls) - 1 : i - 1 : -1]
        st1=""
        for k in ls:
            st1=st1+k
        print(st1)
    
