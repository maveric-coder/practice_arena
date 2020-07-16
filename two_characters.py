import re
def val(ss):
    s1=""
    for i in ss:
        s1=s1+i
    x=[]
    x=re.findall(r'((\w)\2{1,})', s1)
    if x:
        return False
    else:
        return True
n=int(input())
st=input()

s = list(set(st))  
l=0
max_l=0
#print(s)
for x in range(len(s)):
        for y in range(x+1, len(s)):
            cpy = [c for c in st if c==s[x] or c==s[y]]
            #print(cpy)
            if val(cpy):
                max_l = max(max_l, len(cpy))


print(((max_l)))
