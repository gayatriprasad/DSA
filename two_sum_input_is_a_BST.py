# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        traversal = []
        
        self.inorderTraversal(root, traversal)
        
        left = 0 
        right = len(traversal)-1
        # print(right)
        
        while(left < right):
            
            if (traversal[left] + traversal[right] == k):
                return True
            
            elif (traversal[left] + traversal[right] > k):
                right -= 1
                
            else:
                left += 1
                
        return False
        
    def inorderTraversal(self, root: TreeNode, answer):
        
        if root == None:
            return
        
        self.inorderTraversal(root.left, answer)
        answer.append(root.val)
        self.inorderTraversal(root.right, answer)
        
        return 