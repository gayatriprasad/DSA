	#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from queue import Queue

class Solution:

    def topView(self, root):
        # code here
        answer = []
        queue = Queue()
        memo = {}
        
        if root == None:
            return answer

        left = -10000
        right = 10000
        
        queue.put((root, 0))
        
        while(queue):
            
            currentNode, currentHd = queue.get()
            
            memo[currentHd] = currentNode.data
            
            left = min(left, currentHd)
            right = max(right, currentHd)
        
            if currentNode.left:
                queue.put((currentNode.left, currentHd-1))
                
            if currentNode.right:
                queue.put((currentNode.right, currentHd+1))
        
        for i in range(left, right+1):
            answer.append(memo[i])
        
        return answer
