a=str(input())
b=str(input())
n=int(input())
com=0
if  a==b:
    print("Yes")
#elif len(a)>=len(b)+n:
 #   print("No")


else:
    for i in range(min(len(a),len(b))):
        if a[i]==b[i]:
            com+=1
        else:
            break
    maxiter=len(a)+len(b)
    miniter=maxiter-2*com
    if(n>=miniter) and (n-miniter)%2==0:
        print("Yes")
    elif n>=maxiter:
        print("Yes")
    else:
        print("No")
