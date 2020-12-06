def sdev(n):
    x=n
    while x:
        c=x%10
        if c==0 or n%c!=0:
            return False
        
        x//=10
    return True
            
        

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ls=list(range(left,right+1))
        st=[]
        for i in ls:
            if i<10:
                st.append(i)
            else:
                if sdev(i):
                    st.append(i)
        
        return st
        
