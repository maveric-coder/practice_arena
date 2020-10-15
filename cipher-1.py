st=input()
n=int(input())
m=0
if n>26:
    m=n%26
else:
    m=n

ls=""
for i in st:
    if i.isalpha():
        if i.isupper():
            if ord(i)+m>90:
                ls+=(chr((64+(ord(i)+m-90))))
            else:
                ls+=(chr(ord(i)+m))
        else:
            if ord(i)+m>122:
                ls+=(chr(96+(ord(i)+m-122)))
            else:
                ls+=(chr(ord(i)+m))
    elif i.isnumeric():
        if int(i)+n>9:
            ls+=str((int(i)+n)%10)
        else:
            ls+=str(int(i)+n)
    else:
        ls+=i
        
print(ls)
