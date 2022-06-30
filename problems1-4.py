### HASHMAPS : 

## 1. Count of elements in an array

# If we want number of elements simply call len(arr)

## 2. Count distinct elements 

def countElements(arr):
    hashmap = {} 
    For num in arr: 
    if num in arr:
        hashmap[num] += 1
    else: 
        hashmap[num] = 1
    return len(hashmap.keys())


# 3. Intersection of two arrays 

def intersectionArrays(arr1, arr2): 

    intersection = []
    for num in arr1: 
        if num in arr2:
            intersection.append(num)
    
    return intersection
    
    
def intersectionArrays(arr1, arr2): 

    intersection ={}]
    for num in arr1: 
       if num in arr2:
        intersection [num] += 1
       else: 
        intersection [num] = 1
    return intersection.keys()

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def intersection(lst1, lst2):
 
    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


# 4. Union of two array 

def unionArray(arr1, arr2):
    # if repetition is allowed 
    return arr1 + arr2

def unionArray(arr1, arr2):
# if repetition is allowed 
    return list(set(arr1) + set(arr2))
