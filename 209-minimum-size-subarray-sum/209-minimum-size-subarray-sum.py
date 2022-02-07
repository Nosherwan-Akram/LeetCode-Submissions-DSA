class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        res = sys.maxsize
        for r,n in enumerate(nums):
            total += n
            if total < target:                
                continue
            else:
                while total >= target:
                    res = min(r-l+1,res)
                    total -= nums[l]
                    l += 1
        if res == sys.maxsize: return 0
        return res
            