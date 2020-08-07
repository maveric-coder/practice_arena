s=input()
ls=[]
j=0
for i in range(len(s)):
    if s[i].isupper():
        ls.append(s[j:i])
        j=i
print(len(ls)+1)
