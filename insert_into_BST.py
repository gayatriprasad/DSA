# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        if root == None:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
            
        else: 
            root.right = self.insertIntoBST(root.right, val)
            
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    
        # if tree is empty, return the root with given value
        if not root: return TreeNode(val)
        
        # take copy of root, so that we can retain the root
        curNode = root

        # traverse until we found the position of the given value to insert
        while curNode:
            if val < curNode.val:
                if curNode.left:
                    curNode = curNode.left
                else:
                    curNode.left = TreeNode(val)    # add the new value at left of curNode
                    break
            else:
                if curNode.right:
                    curNode = curNode.right
                else:
                    curNode.right = TreeNode(val)   # add the new value at right of curNode
                    break
        
        return root                                  # return root