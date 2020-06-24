cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    if n==1:
        ar1=[0]
    elif n==0:
        ar1=[]    
    else:
        ar1=[0,1]
        for i in range(2,n):
            ar1.append(ar1[i-1]+ar1[i-2])
        
    return ar1



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
