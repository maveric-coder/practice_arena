class Solution:
    def maxPower(self, s: str) -> int:
        c=0
        m=0
        ss=s[0]
        for i in s:
            
            if i ==ss:
                c+=1
            else:
                
                ss=i
                
                c=1
            m=max(m,c)
        return m
                
        
