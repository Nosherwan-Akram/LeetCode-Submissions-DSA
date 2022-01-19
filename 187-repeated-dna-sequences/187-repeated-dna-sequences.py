class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = dict()
        
        for i in range(len(s)):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            else:
                dic[s[i:i+10]] += 1
        res = []
        for k,v in dic.items():
            if v != 1:
                res.append(k)
        return res
        