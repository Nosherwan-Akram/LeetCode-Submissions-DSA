class Solution:
    def makeGood(self, s: str) -> str:
        '''
        
        have a stack and add new strings into it after removing bad chars
        loop over string and if you see bad chars append new string to stack
        start over loop on new string
        '''

        stack = [s]
        
        while True:
            prevStackLen = newStackLen = len(stack[-1])
            for i in range(0,len(stack[-1])-1):
                if (stack[-1][i].isupper() and stack[-1][i].lower() == stack[-1][i+1]) or (stack[-1][i].islower() and stack[-1][i].upper() == stack[-1][i+1]):
                    stack.append(stack[-1][:i]+stack[-1][i+2:])
                    newStackLen += 1
                    break
            if newStackLen == prevStackLen:
                return stack[-1]
            
            