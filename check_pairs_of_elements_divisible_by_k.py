# check if sum of pairs of elements in an array are divisible by k 

# brute force - we will iterate through the array taking each element and sum it with the other elements 
# check if it is divisible by k

# Time - O(n^2) 
# Space - O(n) 

def pairsDivisibleByK(arr, k):
    hashmap = {} 
    
    count = 0 
    
    for num in arr:
        
        rem = ((num % k) + k )) % k
        
        if rem in hashmap:
            hashmap[rem] += 1
        else: 
            hashmap[rem] = 1
            
    for key, val in hashmap.items():
        
        if key == 0:
            if hashmap[key]% 2 == 0:
                return False
        
        elif k-key not in hashmap:
            return False 
        
        elif hashmap[k-key] != hashmap[key]
            return False 
    
    return True
    