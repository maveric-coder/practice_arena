n=int(input())
for _ in range(n):
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())
    bb=0
    ww=0
    bz=0
    wz=0
    bb=b*bc
    ww=wc*w
    wz=w*bc+w*z
    bz=b*wc+b*z
    print(min((bb+ww),(bb+wz),(ww+bz)))
