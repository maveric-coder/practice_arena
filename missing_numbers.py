from collections import Counter
_=int(input())
st=[int(x) for x in input().split()]
_=int(input())
ls=[int(x) for x in input().split()]
a=Counter(st)
b=Counter(ls)
print(*(sorted((b-a).keys())))
