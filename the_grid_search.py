import re

def gridSearch(G, P):
    l = len(P)
    m = len(P[0])
    for x,y in enumerate(G):
        for i in ((m.start(0)) for m in re.finditer("(?=%s)"%P[0], y)):
            for a in range(1,l):
                if G[a+x][i:i+m]!=P[a]:
                    break
            else:
                return "YES"
      
    return "NO"

for _ in range(int(input())):
    R,C = map(int,input().split())
    G = [input() for _ in range(R)]
    r,c = map(int,input().split())
    P = [input() for _ in range(r)]
    print(gridSearch(G, P))
