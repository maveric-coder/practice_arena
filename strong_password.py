import re
n=int(input())
st=input()
x = 0
p = ["[\d]", "[A-Z]", "[a-z]", "[!@#$%^&*()+-]"]
for i in p:
    if not re.search(i, st):
        x+=1
print(max(6-n,x))
