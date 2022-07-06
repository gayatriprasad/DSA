# check if sum of pairs of elements in an array are divisible by k 

# brute force - we will iterate through the array taking each element and sum it with the other elements 
# check if it is divisible by k

# Time - O(n^2) 
# Space - O(n) 

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        hashmap = {}
        for i in arr:
            
            remainder = ((i % k) + k) % k
            # hashmap[remainder] =  hashmap.setdefault(remainder,0) + 1
            if remainder in hashmap:
                hashmap[remainder] += 1
            
            else:
                hashmap[remainder] = 1
   
        for key,val in hashmap.items():
        
            if key == 0:
                
                if hashmap[key] % 2 != 0:
                    return False

            elif k - key not in hashmap:
                return False
            
            elif hashmap[k-key] != hashmap[key]:
                return False
        
        return True