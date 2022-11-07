# 746. Min Cost Climbing Stairs


class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} 
        return min(self.minCost(cost, 0, memo), self.minCost(cost,1 , memo)) 
    
    def minCost(self, cost, currentIndex, memo):
        
        if currentIndex == len(cost):
            return 0
        
        if currentIndex > len(cost):
            return 100001
        
        currentKey = currentIndex
        
        if currentKey in memo:
            return memo[currentKey]
            
            
        oneJump = cost[currentIndex] + self.minCost(cost, currentIndex+1, memo)
        twoJump = cost[currentIndex] + self.minCost(cost, currentIndex+2, memo)
        
        memo[currentKey] = min(oneJump, twoJump) 
        
        return memo[currentKey]