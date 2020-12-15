# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, bits):
            if not root:
                return
            bits += str(root.val)
            if not (root.left or root.right):
                self.res += int(bits,2)
                return
            dfs(root.left, bits)
            dfs(root.right, bits)
            
        dfs(root, '')
        return self.res
        
