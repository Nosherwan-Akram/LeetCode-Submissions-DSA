class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k >= len(nums):
            k = k- len(nums)
        if len(nums)==1 or len(nums)==0 or k==0:
            return
        x = nums[-k:]+nums[:len(nums)-k]
        print(x)
        for i in range(len(x)):
            nums[i] = x[i]
        