def checkBit(pattern,arr, n) : 
    c = 0
    for i in range(0, n) : 
        if ((pattern & int(arr[i])) == pattern) :            
            c = c + 1 

    return c 

for _ in range(int(input())):
    m,n=map(int,input().split())
    ls=list(map(int,input().split()))
    res,cc=0,0
    for bit in range(31,-1,-1) :
        count = checkBit(res | (1 << bit), ls, m) 
        if ( count >= 1 and m-count<=n) : 
            res =res | (1 << bit) 
            cc=m-count
    print(str(res)+" "+str(cc))
