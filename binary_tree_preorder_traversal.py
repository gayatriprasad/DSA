# Binary Tree Preorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        self.helper(root, result)
        
        return result
        
    def helper(self, node: Optional[TreeNode], result: List[int]):
        
        if node == None:
            return
        
        result.append(node.val)
        
        self.helper(node.left, result)
        
        self.helper(node.right, result)
        
    
# TC : O(n)
# SC : O(n+h)


###################### Iterative Method ######################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        elementStack = []
        
        if root == None:
            return answer
        
        elementStack.append(root)
        
        while(len(elementStack) > 0):
            currentNode = elementStack.pop()
            answer.append(currentNode.val)
            
            if (currentNode.right != None):
                elementStack.append(currentNode.right)
            
            if (currentNode.left != None):
                elementStack.append(currentNode.left)
            
        return answer
        