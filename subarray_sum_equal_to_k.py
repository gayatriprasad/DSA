# 974. Subarray Sums Divisible by K 

# Time Complexity : O(N^2) 


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        answer = 0 
        
        for i in range(len(nums)):
            ps = 0
            for j in range(i, len(nums)):
                ps += nums[j]
                
                if ps % k == 0:
                    answer += 1
                    
        return answer
        
        
  # O(N) time 
  
  class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        answer = 0 
        prefixSum = 0 
        
        hashmap = {}
        
        hashmap[prefixSum] = 1 # zero sum is occuring 1 time 
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            rem = ((prefixSum % k) + k) % k 
            
            if rem in hashmap: 
                answer += hashmap[rem]
                hashmap[rem] += 1
            
            else:
                hashmap[rem] = 1
                
        return answer


#  To get the number of subarrays that are not divisible by k : n(n+1)/2 - answer !! 

        
