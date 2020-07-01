_=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
x=[]
count=[]



for i in range(len(a)):
    if a[i] not in x:
        #x.append(a[i])
        count.append(a.count(a[i]))
   
        
#print(x)
#print(count)
#print(max(count))
#print(count.index(max(count)))
print(len(a)-max(count))

