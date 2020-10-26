def cunt(n):
    st=bin(n)[2:]
    return st.count('1')
for _ in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))
    ls.sort(key=cunt)
    print(*ls)
