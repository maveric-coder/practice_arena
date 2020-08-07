s=input()
l=len(s)//3
count=0
i=0
for i in range(0,len(s)-1,3):
    if s[i]!='S':
        count+=1
    if s[i+1]!='O':
        count+=1    
    if s[i+2]!='S':
        count+=1
   
    
print(count)
