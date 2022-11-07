# 697. Degree of an Array 

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # put all elements in a hashmap and get the max frequncy 
        # get the smallest sybarray using the indices

        count={}
        start={}
        end={}
        
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
                start[nums[i]]=i
                end[nums[i]]=i
            else:
                count[nums[i]]+=1
                end[nums[i]]=i
        res=[]
        degree = max(list(count.values()))
        
        for key,value in count.items():
            if value==degree:
                d = end[key]-start[key]+1
                res.append(d)
                
        return min(res)