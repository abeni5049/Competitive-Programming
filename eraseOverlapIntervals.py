class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        for i in range(1,len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i] = intervals[i-1]
                res += 1
        return res
                
