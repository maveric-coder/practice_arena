ls=[67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
for _ in range(int(input())):
    zz=""
    n=int(input())
    st=input()
    m=0
    for i in st:
        
            m=ord(i)
        
            f=1
            xx=m
            yy=m
            while f==1:
                if xx in ls and yy in ls:
                    zz+=chr(yy)
                    f=0
                
                elif xx in ls:
                    zz+=chr(xx)
                    f=0
                elif yy in ls:
                    zz+=chr(yy)
                    f=0
                else:
                    xx+=1
                    yy-=1
        
    print(zz)
