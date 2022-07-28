# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        self.invertTree(root.right) 
        return self.isSameTree(root.left, root.right)
        
            
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return root
        
        rightSubTree = self.invertTree(root.right)
        leftSubTree = self.invertTree(root.left)
        
        root.left = rightSubTree
        root.right = leftSubTree
        
        return root 
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (p == None and q == None):
            return True
        
        if (p == None or q == None or p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        
################### simpler approach ##########################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetricTrees(root.left, root.right)
    
    def symmetricTrees(self, t1, t2):
        
        if (t1 == None and t2 == None):
            return True
        
        if (t1 == None or t2 == None or t1.val != t2.val):
            return False 
        
        return self.symmetricTrees(t1.left, t2.right) and self.symmetricTrees(t1.right, t2.left) 