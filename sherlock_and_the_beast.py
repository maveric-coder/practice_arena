for _ in range(int(input())):
    n=int(input())
    z=n
    while z%3!=0:
        z-=5
    if (z<0):
        print(-1)
    else:
        print(z*'5'+(n-z)*'3')

