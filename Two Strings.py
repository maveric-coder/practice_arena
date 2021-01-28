# Complete the twoStrings function below.
from collections import Counter
def twoStrings(s1, s2):
    a=Counter(s1)
    b=Counter(s2)
    c=0
    for i in b:
        if i in a:
            c+=min(b[i],a[i])
    
    [print ("YES") if c>0 else print ("NO")]
    
            
for _ in range(int(input())):
    s1=input()
    s2=input()
    twoStrings(s1,s2)
