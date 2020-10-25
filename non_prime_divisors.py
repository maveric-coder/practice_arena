def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
import math 

def printDivisors(n): 

    i = 1
    ls=[]
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i == i) : 
                ls.append(i)
            else : 
                ls.append(i)
                ls.append(n//i)
        i = i + 1
    return ls


for _ in range(1):
    n=int(10)
    ls=[]
    ls=printDivisors(n)
    c=0
    for i in ls:
        if not isPrime(i):
            c+=1
    print(c)
