# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root, root.val)
    
    def isSame(self, root, currentVal):
        if root == None:
            return True
        
        if root.val != currentVal:
            return False 
        
        la = self.isSame(root.left, currentVal)
        ra = self.isSame(root.right, currentVal)
        
        
        return la and ra
        