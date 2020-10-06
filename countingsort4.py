def countSort(arr):
    ls={}
    n=len(arr)
    cc=0
    for m in range(n):
        i,j=arr[m]
        i=int(i)
        if i>cc:
            cc=i
        if  m<n/2:
            j="-"
        if  i in ls:
            ls[i].append(j)
        else:
            ls[i]=[j]
    st=[]
    for i in range(cc+1):
        if i in ls:
            for xx in ls[i]:
                st.append(xx)
    print(*st)
