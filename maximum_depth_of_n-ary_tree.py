# Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        
        ans =  0
        for children in root.children:
            tempAns = self.maxDepth(children)
            ans = max(ans, tempAns)
        
        return ans+1