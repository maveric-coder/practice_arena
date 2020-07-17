# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 

n=int(input())
a=map(int, input().split())
it=int(input())

amount=0

shoes = Counter(a)

for i in range (it):
    size,amt=map(int, input().split())
    if shoes[size] > 0:
        amount+=amt
        shoes[size]-=1

print (amount)
