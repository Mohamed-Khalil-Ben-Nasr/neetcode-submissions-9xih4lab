class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        newInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if newInterval[0] <= intervals[i][0] <= newInterval[1]:
                newInterval = [newInterval[0], max(intervals[i][1], newInterval[1])]
            else:
                res.append(newInterval)
                newInterval = intervals[i]

        res.append(newInterval)
        return res