# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # code here
        answer = [] 
        hashmap = {}
        level = 0 
        self.rightView(root, level, hashmap, answer)
        return answer

    def rightView(self, root, level, hashmap, answer):

        if root == None:
            return 

        if level not in hashmap:
            hashmap[level] = 1
            answer.append(root.val)

        self.rightView(root.right, level+1, hashmap, answer)
        self.rightView(root.left, level+1, hashmap, answer)

        return