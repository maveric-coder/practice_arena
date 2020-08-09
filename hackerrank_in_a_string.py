st="hackerrank"
for i in range(int(input())):
    ss=input()
    count=0
    j=k=0
    while j<len(ss) and count<len(st):
        if ss[j]==st[k]:
            j+=1
            k+=1
            count+=1
        else:
            j+=1
    if count==len(st):
        print("YES")
    else:
        print("NO")

