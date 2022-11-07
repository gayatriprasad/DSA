# First Missing Integer

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        try:
            return min(set(range(1, len(A)+1)) - set(A))
        except:
            return max(1, max(A)+1)