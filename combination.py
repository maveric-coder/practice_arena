from itertools import combinations

N = 4
L = "aacd"
K = 2

C = list(combinations(L, K))
count=0
print(C)
for i,j in C:
    if i=='a' or j=='a':
        count+=1
print(count)
print(len(C))
