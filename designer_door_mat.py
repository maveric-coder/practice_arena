n, m = map(int,input().split())
s=".|."
wel = "WELCOME"
for i in range (n//2):
    
    print (((s*i)+s+(s*i)).center(m,"-"))

print (wel.center(m,"-"))

for j in range (n//2):
    t=(n//2)-1
    print (((s*(t-j))+s+(s*(t-j))).center(m,"-"))
