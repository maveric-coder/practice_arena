for _ in range(int(input())):
    
    a=input()
    b=input()
    a+='~'
    b+='~'
    st=""
    i,j=0,0
    while a[i]!='~' or b[j]!='~':
        if a[i]!='~' and a[i:]<b[j:]:
            st+=a[i]
            i+=1
        else:
            st+=b[j]
            j+=1
   
    print(st)
