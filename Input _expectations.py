t= int(input())
ls=[0]*10000000
zz=list(map(int,input().split()))
ss=0
for i in range(t):
    ls[i]=zz[i]
i=0
x=0
while x<t:
    n=ls[i]
    if n==0:
        ss+=1
    #print(str(n)+"as")
    i+=1
    j=0
    while j<n:
        temp=ls[i]
        #print(str(temp)+"asd")
        if temp==0:
            ss+=1
        j+=1
        i+=1
    x+=1
    

print(ss)
