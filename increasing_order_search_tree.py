# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        traversal = []
        self.inorderTraversal(root, traversal)
        
        dummyNode = newRoot = TreeNode(-1)
        
        for num in traversal:
            dummyNode.right = TreeNode(num)
            dummyNode = dummyNode.right
        
        return newRoot.right
    
    
    def inorderTraversal(self, root: TreeNode, answer):
        
        if root == None:
            return
        
        self.inorderTraversal(root.left, answer)
        answer.append(root.val)
        self.inorderTraversal(root.right, answer)
        
        return 
    