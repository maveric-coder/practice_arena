class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ls=[]
        for i in range (len(nums)):
            ls.insert(index[i],nums[i])
        return ls
