class Solution:
    '''
    make a dictionary that holds frequency of each character in string
    2 pointers at start of string
    result = max int
    loop over string
    move right pointer ahead and deduct the characters in sub string from freq dict
    if each char in dict falls below n/4 move left pointer ahead
    after moving left pointer ahead increment the freq dict with characters lost
    from new substring
    when characters in freq dict lower than n/4 update result with min(len(res),subst)
    return after right pointer can't be moved ahead in loop
    '''  
    def balancedString(self, s: str) -> int:
        dic = {'Q':0,'R':0,'W':0,'E':0}
        for p in s:
            dic[p] += 1
        l,r = -1,-1
        res = sys.maxsize
        while (r!=len(s)):
            c = 0
            for k,v in dic.items():
                #if r == 0:
                 #   break
                if v <= len(s)/4:
                    c += 1
                else:
                    c = 0
            if c == 4:
                res = min(res,r-l)
                if res == 0: return 0
                l += 1
                dic[s[l]] += 1
            else:
                r += 1
                if r==len(s): break
                dic[s[r]] -= 1
                
        return res