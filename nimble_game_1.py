for _ in range(int(input())):
    n=int(input())
    ls=[int(x) for x in input().split()]
    ss=0
    for i in range(len(ls)):
            if ls[i]>0:
                if ls[i]%2==0:
                    ss=ss^0
                else:
                    ss=ss^i

    if ss==0:
        print("Second")
    else:
        print("First")
