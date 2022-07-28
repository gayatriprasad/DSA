# N-th Tribonacci Number

class Solution:
    def tribonacci(self, n):

        h={} #creating the dictionary to store the results
        
        def tribo(n):
            if n in h:
                return h[n]
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            else:
                res=tribo(n-3)+tribo(n-2)+tribo(n-1)
                h[n]=res #storing the results so that we can reuse it again
            return res
       
        return tribo(n)
        
        
        
        
#### same solution but might exceed time limits !!! 
class Solution:
    def tribonacci(self, n):

        if n==0:
            return 0
        
        elif n==1 or n==2:
            return 1
        
        else:
            res=self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
        
        return res
       