n=int(input())
ls=[]
for _ in range(n):
    ls.append((input()))
ls.sort(key = lambda x: (len(x), x)) 
for s in ls:
    print(s)
