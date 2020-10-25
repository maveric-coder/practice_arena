    
for _ in range(int(input())):
    n=int(input())
    ls=[int(x) for x in input().split()]
    ls=sorted(ls,reverse=True)
    
    ls=list(filter(lambda x : x > 0, ls)) 
    s=sum(ls)


    bb=len(bin(s)[2:]) -1
    
    res=bin(pow(2,bb))[2:]
    if int(res,2) == s: 
        print('Yes') 
    else: 
        print('No')
