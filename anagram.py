from collections import Counter

for _ in range(int(input())):
    st=input()
    if len(st)%2==1:
        print(-1)
    else:
        n=len(st)//2
        a=Counter(st[:n])
        b=Counter(st[n:])
        print(n-sum((a & b).values()))
