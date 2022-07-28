# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.isPossible(root, targetSum, 0)
    
    def isPossible(self, root, targetSum, currentSum):
        
        if root == None:
            return False
        if (root.left == None and root.right == None): 
            return currentSum + root.val == targetSum
        
        return self.isPossible(root.left, targetSum, currentSum + root.val) or self.isPossible(root.right, targetSum, currentSum + root.val) 