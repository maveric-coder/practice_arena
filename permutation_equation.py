n=int(input())
ls = [int(x) for x in input().split()]

#ar=[]
#print(ls[0])
for i in range(1,n+1):
    
    x=ls.index(i)+1
    y=ls.index(x)+1
    print(y)
