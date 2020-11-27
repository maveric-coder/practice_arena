for _ in range(int(input())):
    x,y=map(int,input().split())
    print(x+y+max(0,(abs(x-y)-1)))
