# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

b,g=map(float,input().split())
odds=b/g
b=odds/(1+odds)
g=1-b
s=0
for i in range(3,7):
    s=s+(comb(6,i)*pow(b,i)*pow(g,(6-i)))
print(round(s,3))



