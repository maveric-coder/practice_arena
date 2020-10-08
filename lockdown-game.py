n=int(input())
s=input()
ls=list(range(1,n+1))
i=0
j=0
while len(ls)!=1:

    if s[j]=='y':
        ls.remove(ls[i])
        i-=1
    if j==len(s)-1:
        j=0
    else:
        j+=1
    if i==len(ls)-1:
        i=0
    else:
        i+=1

print(*ls)
