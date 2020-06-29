import math

for _ in range(int(input())):
    m,n=map(int,input().split())
    count=0
    while(m<=n):
    
        #if bool(re.match(r'[0-9]*[.]0$',y)):
        if float.is_integer(math.sqrt(m)):
            count+=1
            m=(m//math.sqrt(m)+1)**2
        else:
            m+=1
    print(count)



    
