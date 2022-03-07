class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*k
        m=len(nums1);n=len(nums2)
        for i in range(0,k+1):
            j=k-i
            if i>m or j>n:
                continue
            res1 = self.getMaxNumber(nums1, i)
            res2 = self.getMaxNumber(nums2, j)
            merged = self.MergeMaxNums(res1, res2)
            res = max(merged, res)
        return res[:k]
        
    def MergeMaxNums(self, n1, n2):
        r = []
        while (n1 or n2):
            if n1>n2:
                r.append(n1[0])
                n1=n1[1:]
            else:
                r.append(n2[0])
                n2=n2[1:]
        return r
        
    def getMaxNumber(self, nums, L):
        stack = []
        i=0
        while i<len(nums):
            remain = len(nums)-i
            while len(stack) and nums[i]>stack[-1] and L<remain:
                L+=1
                stack.pop()
            L-=1
            stack.append(nums[i])
            i+=1
        return stack