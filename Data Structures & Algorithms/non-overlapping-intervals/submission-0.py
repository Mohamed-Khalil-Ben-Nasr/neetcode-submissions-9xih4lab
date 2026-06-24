class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        # sort => O(nlogn)
        intervals.sort(key= lambda x: x[0])

        res = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            # if there is overlap
            if interval[0] < end:
                res += 1
                end = min(end, interval[1])
            # there is no overlap
            else:
                end = interval[1]
        return res
            
            