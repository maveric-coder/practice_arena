_=input()
st=input()
j=0
count=0
while j<len(st):
    if st[j:j+3]=='010':
        count+=1
        j+=3
    else:
        j+=1
print(count)
