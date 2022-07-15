# 1022. Sum of Root To Leaf Binary Numbers


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        answer = []
        self.rootToLeaf(root, "", answer)
        return sum(answer)
    
    
    def rootToLeaf(self, root, currentString, answer):
        
        if (root.left == None) and (root.right == None):
            currentString += str(root.val)
            answer.append(int(currentString, 2))
            return
        
        if root.left != None:
            self.rootToLeaf(root.left, currentString + str(root.val), answer)
        
        if root.right != None:
            self.rootToLeaf(root.right, currentString + str(root.val), answer)
            
        return 
        
        
        