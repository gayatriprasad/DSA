### GFG 

##Reverse words in a given string

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        wordList = S.split('.')
        # print(wordList)
        wordListRev = wordList[::-1]
        
        answer = '.'.join(wordListRev)    # print(answer)
        return answer 