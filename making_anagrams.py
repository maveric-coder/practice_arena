from collections import Counter
s1=input()
s2=input()
a=Counter(s1)
a.subtract(s2)
print(sum(abs(x) for x in a.values()))
