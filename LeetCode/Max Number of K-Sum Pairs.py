class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ls=sorted([num for num in nums if num<k])
        l,r=0,len(ls)-1
        c=0
        while l<r:
            s=ls[l]+ls[r]
            if s==k:
                l+=1
                r-=1
                c+=1
            elif s<k:
                l+=1
            else:
                r-=1
        return c
        
        
