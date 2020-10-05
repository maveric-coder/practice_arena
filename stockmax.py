def stockmax(p):
    c=p[len(p)-1]
    a=0
    for i in range(len(p)-1,-1,-1):
        if c<p[i]:
            c=p[i]
        a+=(c-p[i])
    return a
