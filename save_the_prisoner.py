for _ in range(int(input())):
    n,m,s=input().strip().split()
    n=int(n)
    m=int(m)
    s=int(s)
    if((m+s-1)%n==0):
        print(n)
    else:
        print((m+s-1)%n)
