# 429. N-ary Tree Level Order Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            
                for child in currentNode.children:
                    queueList.put(child)
            
            answer.append(level)
            
        return answer  