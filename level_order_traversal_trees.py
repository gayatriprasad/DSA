# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        queueList = Queue()
        
        if root == None:
            return answer
        
        queueList.put(root)
        
        while(queueList.empty()):
            currentNode = queue.get()
            asnwer.add(currentNode.val)
            
            if currentNode.left != None:
                queueList.put(currentNode.left)
                
            if currentNode.right != None:
                queueList.put(currentNode.right)
            
        return answer