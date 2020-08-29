import math as ma

n=int(input())
ls=[int(x) for x in input().split()]
x=sum(ls)/n

ss=[]
for i in range(n):
    ss.append((ls[i]-x)**2)

print(round((ma.sqrt(sum(ss)/n)),1))
