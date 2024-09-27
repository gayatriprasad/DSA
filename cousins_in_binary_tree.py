# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        levels = [None] * 2
        levels[0], levels[1] = -1, -1 # zeroth level is for x, first level is for y 
        parents = [None] * 2
        parents[0], parents [1] = -1, -1 # zeroth parent is for x, first parent is for y
        
        self.findNodes(root, x,y, levels, parents, 0, None)
        
        if (levels[0] == levels[1] and parents[0] != parents[1]):
            return True
        
        return False
    
    def findNodes(self, root, x, y, levels, parents, currentLevel, currentParent):
        
        if root == None:
            return 
        
        if (root.val == x): 
            levels[0] = currentLevel
            parents[0] = currentParent
            
        if (root.val == y):
            levels[1] = currentLevel
            parents[1] = currentParent
            
        self.findNodes(root.left, x,y, levels, parents, currentLevel+1, root)
        self.findNodes(root.right, x,y,levels, parents, currentLevel+1, root)
        
        return 