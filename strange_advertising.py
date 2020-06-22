import math
count=0
n=5
for i in range(int(input())):
    like=math.floor(n/2)
    count+=like
    sh=like*3
    n=sh



print(count)
