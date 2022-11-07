# 198. House Robber


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} 
        return self.maxMoney(nums, 0, memo)

    def maxMoney(self, nums, currentHouse, memo):

        if currentHouse >= len(nums):
            return 0

        currentKey = currentHouse

        if currentKey in memo:
            return memo[currentKey]

        
        rob = nums[currentHouse] + self.maxMoney(nums, currentHouse + 2, memo)
        noRob = self.maxMoney(nums, currentHouse + 1, memo)

        memo[currentKey] = max(rob, noRob) 

        return memo[currentKey]