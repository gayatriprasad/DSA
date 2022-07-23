# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        self.helper(root, result)
        
        return result
        
    def helper(self, node: Optional[TreeNode], result: List[int]):
        
        if node == None:
            return
             
        self.helper(node.left, result)
       
        result.append(node.val)
        
        self.helper(node.right, result)
       
# TC : O(n)
# SC : O(n+h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer = [] 
        eStack = []
        
        if root == None:
            return answer
        
        self.addLeftSubTree(root,eStack)
        
        while(eStack):

            currentNode = eStack.pop()
            answer.append(currentNode.val)
            
            if (currentNode.right != None):
                self.addLeftSubTree(currentNode.right, eStack)
                
        return answer
    
    def addLeftSubTree(self, currentNode, eStack):
        
        eStack.append(currentNode)
        
        while(currentNode.left != None):
            eStack.append(currentNode.left)
            currentNode = currentNode.left
        
        return
    