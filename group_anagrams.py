# 49. Group Anagrams 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        m = {}
        for currentString in strs:
            memo = [0 for _ in range(26)]
            
            for currentChar in currentString: 
                currentIndex = ord(currentChar) - ord('a')
                memo[currentIndex] += 1
            
            if tuple(memo)in m:
                m[tuple(memo)].append(currentString)
                
            else: 
                m[tuple(memo)] = [currentString]
                
        return list(m.values())