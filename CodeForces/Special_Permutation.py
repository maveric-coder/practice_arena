for _ in range(int(input())):
    n=int(input())
    st=[]
    for i in range(n):
        st.append((i+1)%n+1)
    print(*st)
