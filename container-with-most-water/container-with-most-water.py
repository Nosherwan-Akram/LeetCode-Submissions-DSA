class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        p1 = 0
        p2 = len(height) - 1
        while p1!=p2:
            width = p2-p1
            if height[p1]>height[p2]:
                h = height[p2]
                p2 -= 1
            else:
                h = height[p1]
                p1 += 1
            area = max(area,h*width)
        return area