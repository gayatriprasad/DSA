# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from queue import Queue

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        queueList = Queue()
        
        if root == None:
            return answer
        
        queueList.put(root)
        
        currentSize = 0
        while(not queueList.empty()):
            currentSize = queueList.qsize()
            level = []
            
            while (currentSize > 0):
                
                currentNode = queueList.get()
                level.append(currentNode.val)
                currentSize -= 1
            
                if currentNode.left != None:
                    queueList.put(currentNode.left)
                
                if currentNode.right != None:
                    queueList.put(currentNode.right)
            
            answer.append(level)
            
        return answer[::-1] 