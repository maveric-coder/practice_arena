
import re
def happy(n,st):
    if st.count("_") == 0 and len(re.sub(r'((.)\2+)', "", st)) != 0:
        return "NO"
    for i in st:
        if i != "_" and st.count(i) == 1:
            return "NO"
    return "YES"
for j in range(int(input())):
    n=int(input())
    st=input()
    print(happy(n,st))
    
