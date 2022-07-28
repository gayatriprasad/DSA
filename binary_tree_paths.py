# 257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        
        self.rootToLeaf(root, "", answer);
        return answer
    
    def rootToLeaf(self, root, currentPath, answer):
        
        if root == None:
            return 
        
        if (root.left == None and root.right == None):
            currentPath += str(root.val)
            answer.append(currentPath)
            
        currentPath = currentPath + str(root.val) + "->"
        
        self.rootToLeaf(root.left, currentPath, answer)
        self.rootToLeaf(root.right, currentPath, answer)
        
        return 