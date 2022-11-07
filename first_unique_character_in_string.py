# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use a hashmap to return the first non entry 

        memo = {} 

        for i in range( 0, len(s)):
            
            if s[i] in memo:
                memo[s[i]] += 1
            
            if s[i] not in memo:
                memo[s[i]] = 1
            
        for key, value in memo.items():
            if value == 1:
                return s.index(key)
        