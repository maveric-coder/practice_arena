n=7
m=21
s=".|."
wel = "WELCOME"
for i in range (int(n/2)):
    
    print (((s*i)+s+(s*i)).center(m,"-"))

print (wel.center(m,"-"))

for j in range (int(n/2)):
    t=int(n/2)-1
    print (((s*(t-j))+s+(s*(t-j))).center(m,"-"))
