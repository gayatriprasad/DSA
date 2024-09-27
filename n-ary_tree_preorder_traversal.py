# N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        self.helper(root, result)
        
        return result
        
    def helper(self, node: Optional[TreeNode], result: List[int]):
        
        if node == None:
            return
        
        result.append(node.val)
        
        for child in node.children:
            
            self.helper(child, result)
        
# TC : O(n)
# SC : O(n+h)

###################### Iterative Method ######################


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        elementStack = []
        
        if root == None:
            return answer
        
        elementStack.append(root)
        
        while(elementStack):
            currentNode = elementStack.pop()
            answer.append(currentNode.val)
            
            childList = currentNode.children
            n = len(childList)
            
            for i in range(n-1, -1, -1):
            
                elementStack.append(childList[i])
            
            
        return answer