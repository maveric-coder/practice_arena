n=int(input())
ls=[int(x)for x in input().split()]

count=-1
i=0
while i<n:
    count+=1
    if i<n-2 and ls[i+2]==0:
        i+=1
    i+=1


print(count)

            

    


