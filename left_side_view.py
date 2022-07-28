# Left View of Binary Tree

# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    answer = [] 
    hashmap = {}
    level = 0
    leftSideView(root, level, hashmap, answer)
    return answer
    
def leftSideView( root, level, hashmap, answer):
    
    if root == None:
        return 
    
    if level not in hashmap:
        hashmap[level] = 1
        answer.append(root.data)
        
    leftSideView(root.left, level+1, hashmap, answer)
    leftSideView(root.right, level+1, hashmap, answer)
    
    return