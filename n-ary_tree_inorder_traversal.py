
# Python3 implementation of the approach
class Solution:
     
    # Class for the node of the tree
    class Node:
        def __init__(self, n, data):
            # List of children
            self.children = [None]*n
            self.data = data
     
    # Function to print the inorder traversal of the n-ary tree
    
	def inorderTraversal(self, node):
        
        result = []
        self.helper(node, result)
        return result
    
	def helper(self, node, answer):
        if node == None:
            return
         
        # Total children count
        total = len(node.children)
         
        # All the children except the last
        for i in range(total-1):
            self.inorder(node.children[i])
         
        answer.append(node.data)
         
        # Last child
        self.inorder(node.children[total-1])
     