from math import factorial
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

b,g=map(float,input().split())
b=0.12
g=0.88
s=0
for i in range(0,3):
    s=s+(comb(10,i)*pow(b,i)*pow(g,(10-i)))
print(round(s,3))

s=0
for i in range(2,11):
    s=s+(comb(10,i)*pow(b,i)*pow(g,(10-i)))
print(round(s,3))
