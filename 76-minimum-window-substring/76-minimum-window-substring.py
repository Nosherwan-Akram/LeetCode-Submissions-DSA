class Solution:
    '''
    make freq dict of string 't'
    pointer l,r at -1
    loop over s till r<len(s)
        flag = true
        loop over freq dict
            check if value > 0
                flag = false
        if flag is true 
            res = min(res,r-l)
            r += 1
        else
            l += 1
    return s[l:r]
        
    '''
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        org = Counter(s)
        for j,k in dic.items():
            if k > org[j]:
                return ''
        l,r = 0,0
        res = s
        while (r<=len(s)):
            c = 0
            for k,v in dic.items():
                if v <= 0:
                    c += 1
            if c != len(dic):                
                if r == len(s): break
                if s[r] in dic: dic[s[r]] -= 1
                r += 1
            else:                
                if s[l] in dic: dic[s[l]] += 1
                res = min(res,s[l:r],key=len)
                l += 1                
       # res = min(s[l:r],res,key=len)
        return res