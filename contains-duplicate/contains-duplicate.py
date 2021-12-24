class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i, num in enumerate((nums)):
            if num not in s:
                s.add(num)
            else:
                return 1
        return 0
                
        