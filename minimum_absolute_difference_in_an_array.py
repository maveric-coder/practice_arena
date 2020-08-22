
_=input()
ls=sorted([int(x) for x in input().split()])
m=max(ls)
for i in range(len(ls)-1):
    s=ls[i+1]-ls[i]
    if m>s:
        m=s

print(m)
