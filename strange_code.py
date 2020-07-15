from math import ceil
n=int(input())

x=3
s=4
if n>3:
    while s<=n:
        a=s
        x=x*2
        s=a+x
    print(s-n)
else:
    print(4-n)


