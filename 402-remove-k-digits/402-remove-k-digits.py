class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        1 - can k be neagative, can k b 0
        2 - wht if num starts with 0
        3 - highes num, k
        4 - lowest num, k
        5 - k is bigger than len of num
        
        [1,2,1,9]
        [1140]
        '''
        if len(num) == k: return '0'
        stack = []
        for c in num:
            while stack and stack[-1] > c and k != 0:
                stack.pop()
                k -= 1      
            stack.append(c)
            
        if k: stack = stack[0:-k]
        return str(int(''.join(stack)))