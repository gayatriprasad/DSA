# 863. All Nodes Distance K in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = []
        parentHash = {}
        hashSet = []
        
        self.populateParentMap(root, None, parentHash)
        self.printKDistance(target, k, hashSet, parentHash, answer)
        return answer
    
    def populateParentMap(self, currentNode, currentParent, parentHash):
        
        if currentNode == None:
            return 
    
        parentHash[currentNode] = currentParent
        self.populateParentMap(currentNode.left, currentNode, parentHash)
        self.populateParentMap(currentNode.right, currentNode, parentHash)
    
        return 
    
    
    def printKDistance(self, currentNode, k, hashSet, parentHash, answer):
        
        if (currentNode == None or currentNode in hashSet or k < 0):
            return 
    
        hashSet.append(currentNode)
        
        if (k == 0):
            answer.append(currentNode.val)
            return
        
        self.printKDistance(currentNode.left, k-1, hashSet, parentHash, answer)
        self.printKDistance(currentNode.right, k-1, hashSet, parentHash, answer)
        self.printKDistance(parentHash[currentNode], k-1, hashSet, parentHash, answer)
            
        return 
    
    
# SC : O(n) + O(n) + O(x)
# TC : O(n)