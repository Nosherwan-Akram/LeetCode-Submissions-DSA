class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i,c in enumerate(s):
            if c not in freq:
                freq[c] = i
            else:
                freq[c] = -1
        for k,v in freq.items():
            if v != -1:
                return v
        else: return -1