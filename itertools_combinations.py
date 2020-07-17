# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,l=input().split()
st=sorted(s)
ls = []

for i in range(1, int(l) + 1):
    ls += list(combinations(st, i))

for i in ls:
    print("".join(i))
