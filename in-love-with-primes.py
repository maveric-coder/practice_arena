def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

for _ in range(int(input())):
    n=int(input())
    f=0
    for i in range(2,n):
        a=i 
        b=n-i
        if isPrime(a) and isPrime(b):
            f=1
            print("Deepa")
            break
    if f==0:
        print("Arjit")
