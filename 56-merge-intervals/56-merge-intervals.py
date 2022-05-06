class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0] and res[-1][1] < intervals[i][1]:
                res[-1] = ([res[-1][0],intervals[i][1]])
            elif res[-1][1] >= intervals[i][0] and res[-1][1] >= intervals[i][1]:
                continue
            else:
                res.append(intervals[i])
            
        return res
    