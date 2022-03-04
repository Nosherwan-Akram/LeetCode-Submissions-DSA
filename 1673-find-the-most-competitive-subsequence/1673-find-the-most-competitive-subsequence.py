class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i,n in enumerate(nums):
            while s and s[-1] > n and k-len(s) <= len(nums) - i -1:
                s.pop()
            if len(s) < k: s.append(n)
        return s