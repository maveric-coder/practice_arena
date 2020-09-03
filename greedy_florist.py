def getMinimumCost(k, c):
    n=len(c)
    ls=sorted(c,reverse=True)
    t=0
    for i in range(n):
        t+=(int(i/k)+1)*ls[i]
    return t
