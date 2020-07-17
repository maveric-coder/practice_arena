n=int(input())
ls=[input() for _ in range(n)]
print(ls[0])
if n>1:
    for i in range(1,n-1):
        st=""
        for j in range(0,n):
            if j==0 or j==n-1:
                st=st+ls[i][j]
            else:
                if ls[i][j]>ls[i][j-1] and ls[i][j]>ls[i][j+1] and ls[i][j]>ls[i+1][j] and ls[i][j]>ls[i-1][j]:
                    st=st+'X'
                else:
                    st=st+ls[i][j]
        print(st)

        
    print(ls[n-1])
