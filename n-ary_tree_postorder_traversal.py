# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        self.helper(root, result)
        
        return result
        
    def helper(self, node: Optional[TreeNode], result: List[int]):
        
        if node == None:
            return
        
       
        for child in node.children:
            
            self.helper(child, result)
            
        result.append(node.val)

# TC : O(n)