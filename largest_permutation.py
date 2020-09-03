def largestPermutation(k, arr):
    ls=arr
    st=sorted(arr,reverse=True)
    n=0
    j,i=0,0
    if st==ls:
        return ls
    while n<k and i<len(ls):
        if ls[i]==max(st):
            i+=1
            st=st[1:]
        else:
            ls[ls.index(max(st))],ls[i]=ls[i],ls[ls.index(max(st))]
            st=st[1:]
            n+=1
            i+=1
    return ls
    
    
    
    
    def largestPermutation(k, arr):
    d = {k:v for v, k in enumerate(arr)}
    i = 0
    m = len(arr)
    while k > 0 and m > 1:
        if arr[i] != m:
            arr[i], arr[d[m]] = arr[d[m]], arr[i]
            d[arr[d[m]]], d[m] = d[m], i          
            k -= 1
        m -= 1
        i += 1
    return arr
