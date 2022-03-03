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
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n is not '0': # prevent leading zeros
                st.append(n)
                
        if k: # not fully spent
            st = st[0:-k]
            
        return ''.join(st) or '0'