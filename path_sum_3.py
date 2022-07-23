# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if root is None:
            return 0
        
        return self.pathSumUtil(root, targetSum)
    
    def pathSumUtil(self, root, targetSum):
        
        if root is None:
            return 0
        
        a = self.checkTarget(root, 0, targetSum)
        a = self.pathSumUtil(root.left, targetSum)
        a = self.pathSumUtil(root.right, targetSum)
    
    
    def checkTarget(self, root, 0, targetSum):
        
        
        
        