"""
##### DSA_Python

Data Structures and Algorithms in Python 

The repo contains practise problems for Data Strucutes and Algorithms. 

The problems are solved in Python and are taken mainly from LeetCode, GeeksForGeeks, PepCoding.

"""
################################### Problem 1  #######################################

# 1497. Check If Array Pairs Are Divisible by k

########################## Using Lists  #############################   

# Time Complexity O(n+k)
# Space Complexity O(k)

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        memo = [0 for _ in range(k)]
        n = len(arr)
        
        for i in range(n):
            currentVal = arr[i]
            currentRem = ((currentVal%k)+k)%k
            memo[currentRem] += 1
            
        
        for i in range(k):
            
            if i ==0 :
                if memo[i] % 2:
                    return False
            else: 
                comp  = k-i
                
                if memo[i] != memo[comp]:
                    return False
                
        return True
        
########################## Using Hashmaps  ############################

# Time Complexity O(n+k)
# Space Complexity O(k)

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        dic = {}
        
        for i in arr:
            
            remainder = ((i % k) + k) % k

            if remainder in dic:
                dic[remainder] += 1
            
            else:
                dic[remainder] = 1
   
        for key in dic.keys():
        
            if key == 0:
                
                if dic[key] % 2 != 0:
                    return False

            elif k - key not in dic:
                return False
            
            elif dic[k-key] != dic[key]:
                return False
        
        return True
        
        
        
################################### Problem 2  #######################################

# Brute force : Generate all subarrays - O(n^2) and  calculate sum O(n) - total O(n^3) 

# Slightly better approach : Generate all subarrays - O(n^2) and  calculate sum O(1) while generting arrays - total O(n^2)

# Optimal approach 

# Time Commplexity : O(n) time
 
def maxLen(arr):
     
    # Create an empty hash map (dictionary)
    hash_map = {}
 
    # Initialize result
    max_len = 0
 
    # Initialize sum of elements
    curr_sum = 0
 
    # Initialize count for number of subarrays with sum 0
    curr_sum = 0
    
    # Traverse through the given array
    for i in range(len(arr)):
         
        # Add the current element to the sum
        curr_sum += arr[i]
 
        # to deal woth first element being zero 
        if arr[i] is 0 and max_len is 0:
            max_len = 1
 
        if curr_sum is 0:
            max_len = i + 1
 
        # NOTE: 'in' operation in dictionary to search key takes O(1). Look if current sum is seen before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum] )
        else:
 
            # else put this sum in dictionary
            hash_map[curr_sum] = i
 
    return max_len
 
 
 ################################### Problem 3  #######################################

# Brute force : Generate all subarrays - O(n^2) and  calculate sum O(n) - total O(n^3) 

# Slightly better approach : Generate all subarrays - O(n^2) and  calculate sum O(1) while generting arrays - total O(n^2)

# Optimal approach 

# Time Commplexity : O(n) time
 
  class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        memo = {}
        prefixSum = answer = 0
        
        memo[prefixSum] = 1
        
        for i in range(n):
            currentVal = arr[i]
            prefixSum += currentVal
            
            if prefixSum in memo:
                answer += memo[prefixSum]
                memo[prefixSum] += 1                
            else:
                memo[prefixSum] = 1
        return answer
        
  

################################### Problem 4  #######################################
#### Count distinct elements in every window 
 
  class Solution:
    def countDistinct(self, nums, n, k):
        # Code here
        hashmap = {}
        distinctCount = 0 
        answer = []
        
        for i in range(k-1):
            currentVal = nums[i]
            
            if currentVal in hashmap:
                hashmap[currentVal] += 1
            else:
                hashmap[currentVal] = 1
                distinctCount += 1
            
        release = 0 
        
        for acquire in range(k-1,n):
            currentVal = nums[acquire]
            
            if currentVal in hashmap:
                hashmap[currentVal] += 1
            else:
                hashmap[currentVal] = 1
                distinctCount += 1
            
            answer.append(distinctCount)
            
            disVal = nums[release]
            hashmap[disVal] -= 1
            
            if hashmap[disVal] == 0:
                del hashmap[disVal]
                distinctCount -= 1
            release += 1
        
        return answer
        
        
################################### Problem 5  #######################################
#### Length of the longest substring without repeating characters

# Brute force approach: 
# O(n^3)  
 
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        answer = -1 
        left = 0 
        hashmap = {}
        
        for right in range(len(s)):
            currentChar = s[right]
            
            if currentChar in hashmap:
                hashmap[currentChar] += 1
            else: 
                hashmap[currentChar] = 1
            
            while left <= right and len(hashmap) > k:
                disChar = s[left]
                hashmap[disChar] -= 1
                left += 1
                
                if hashmap[disChar] == 0:
                    del hashmap[disChar]
            
            if len(hashmap)== k:
                answer = max(answer, right-left+1)
        return answer
        
 
################################### Problem 6  #######################################
#### 
### similar to problem where we count number of subarrays with zero sum

 class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        memo = {}
        prefixSum = answer = 0
        
        memo[prefixSum] = 1
        
        for i in range(0, n):
            currentVal = arr[i]
            
            if currentVal == 0:
                prefixSum += -1
            
            else:
                prefixSum += 1
                
            if prefixSum in memo:
                answer += memo[prefixSum]
                memo[prefixSum] += 1                
            
            else:
                memo[prefixSum] = 1
        
        return answer        


################################### Problem 8  #######################################
#### 
### Longest Subarray With Equal Number Of 0s 1s And 2s


def largestSubarry(nums):
    countZeros = countOnes = countTwos= 0
    hashmap= {}
    ans = 0
        
    key = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
    hashmap[key] = -1 
        
    for i in range(len(nums)):
            
        if nums[i] == 0:
            countZeros += 1
                
        elif nums[i] == 1:
            countOnes+=1
            
        else:
            countTwos += 1
            
        currentKey = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
            
        if currentKey in hashmap:
            prevIndex = hashmap[currentKey]
            length = i = prevIndex
            answer = max(answer, length)
    return ans
    
    
    
################################### Problem 9  #######################################
#### 
### Longest Subarray With Equal Number Of 0s 1s And 2s 

class Solution:

    def getSubstringWithEqual012(self, s):
        countZeros = countOnes = countTwos= 0
        hashmap= {}
        ans = 0
        
        key = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
        # key where occurance of 0 # 0 is 1  
        hashmap[key] = 1 
        
        for i in range(len(s)):
            
            if s[i] == '0':
                countZeros += 1
                
            elif s[i] == '1':
                countOnes+=1
            
            else:
                countTwos += 1
            
            currentKey = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
            
            if currentKey in hashmap:
                ans += hashmap[currentKey]
                hashmap[currentKey] += 1
            else:
                hashmap[currentKey] = 1
                
        return ans



################################### Problem 10  #######################################
#### 
### Subarray Sum Equals K

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        answer, prefixSum = 0, 0
        hashmap ={}
        
        hashmap[prefixSum] = 1 # for count = 0 
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if(prefixSum-k) in hashmap:
                answer += hashmap[prefixSum-k]
            
            if prefixSum in hashmap:
                hashmap[prefixSum] += 1
            else:
                hashmap[prefixSum] = 1
        
        return answer