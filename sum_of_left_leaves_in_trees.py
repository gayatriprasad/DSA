# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumOfLeftInLeaves(root, False)
    
    def sumOfLeftInLeaves(self, root, isLeft):
        
        if root == None:
            return 0
        
        if root.left is None and root.right is None and isLeft is True:
            return root.val
        
        leftAns = self.sumOfLeftInLeaves(root.left, True)
        rightAns = self.sumOfLeftInLeaves(root.right, False)
        
        return leftAns + rightAns