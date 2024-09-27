# Print all nodes that don't have sibling

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    answer = []
    self.findNoSiblings(root, answer)
    if len(answer)  == 0:
        return [-1]
    return sorted(answer)
    
def findNoSiblings(self, root, answer):
        
    if root == None:
        return 
        
    if (root.left == None and root.right == None):
        return 
        
    if (root.left != None and root.right != None):
        self.findNoSiblings(root.left, answer)
        self.findNoSiblings(root.right, answer)
    
    elif (root.left != None):
        answer.append(root.left)
        self.findNoSiblings(root.left, answer)
    
    elif (root.right != None):
        answer.append(root.right)
        self.findNoSiblings(root.right, answer)
        
    return