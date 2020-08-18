for _ in range(int(input())):
    n=int(input())
    ls=[int(x) for x in input().split()]
    ss=ls[0]
    for i in range(1,len(ls)):
            ss=ss^ls[i]

    if ss==0:
        print("Second")
    else:
        print("First")
