ls=[6,2,5,5,4,5,6,3,7,6]
for _ in range(int(input())):
    n=str(input())
    s=0
    for i in n:
        
        s+=ls[int(i)]

    if s%2==0:
        print("1"*(s//2))
    else:
        print("7"+"1"*((s//2)-1))
