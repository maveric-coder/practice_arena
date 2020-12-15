class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        s2=sorted(s2)
        f1=0
        f2=0
        for i in range(len(s1)):
            if s2[i]<s1[i]:
                f1=1
                break
        for i in range(len(s1)):
            if s2[i]>s1[i]:
                f2=1
                break
        if f1==1 and f2==1:
            return False
        else:
            return True
        
