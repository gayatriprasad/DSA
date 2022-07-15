# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafTree1 = []
        leafTree2 = []
        
        leafTree1 = self.getLeaf(root1, leafTree1)
        leafTree2 = self.getLeaf(root2, leafTree2)
        if leafTree1 == leafTree2:
            return True
        return False
    
    def getLeaf(self, root, leafTree):
        
        if root == None:
            return False 
        
        if root.left == None and root.right == None:
            leafTree.append(root.val)
            
        self.getLeaf(root.left, leafTree)
        self.getLeaf(root.right, leafTree)
        
        return leafTree
        
