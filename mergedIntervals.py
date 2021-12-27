class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        arr = []
        for i in range(len(intervals)):
            if not arr or arr[-1][1] < intervals[i][0]:
                arr.append(intervals[i])
            elif arr[-1][1] < intervals[i][1]:
                arr[-1][1] = intervals[i][1]
            else:
                arr[-1][1] = arr[-1][1]
        return arr
    