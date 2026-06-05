class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endIdx = None
        res = 0
        for interval in intervals:
            if endIdx and endIdx > interval[0]:
                endIdx = min(endIdx, interval[1])
                res += 1
            else:
                endIdx = interval[1]
        
        return res