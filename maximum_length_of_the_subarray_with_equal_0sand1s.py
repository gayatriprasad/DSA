################################### Problem 7  #######################################
# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray # with equal 0s and 1s
class Solution:
    def maxLen(self,arr, n):
        # code here
         
        # Create an empty hash map (dictionary)
        hash_map = {}
     
        # Initialize result
        max_len = 0
     
        # Initialize sum of elements
        curr_sum = 0
     
        # Traverse through the given array
        for i in range(n):
             
            # Add the current element to the sum
            currentVal = arr[i]
            
            if currentVal == 0:
                curr_sum += -1
            else:
                curr_sum += 1
     
            if curr_sum is 0:
                max_len = i + 1
     
            # NOTE: 'in' operation in dictionary to search key takes O(1). Look if current sum is seen before
            if curr_sum in hash_map:
                max_len = max(max_len, i - hash_map[curr_sum] )
            else:
     
                # else put this sum in dictionary
                hash_map[curr_sum] = i
     
        return max_len
 