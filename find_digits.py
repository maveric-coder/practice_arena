for _ in range(int(input())):
    x=int(input())
    y=x
    temp=y
    count=0
    while y>0:
        temp=y%10
        if temp>0:
            if x%temp==0:
                count+=1
        y=int(y/10)
    print(count)

