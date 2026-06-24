class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []
        for i, interval in enumerate(intervals):
            # if end of current interval < start of the newInterval
            # => cant merge
            if interval[1] < newInterval[0]:
                res.append(interval)
                if i == len(intervals)-1:
                    res.append(newInterval)
            # if current interval start > end of the the newInterval
            # => cant merge anymore => break
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # the current interval and newInterval overlap
            # => merge
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                if i == len(intervals)-1:
                    res.append(newInterval)

        return res